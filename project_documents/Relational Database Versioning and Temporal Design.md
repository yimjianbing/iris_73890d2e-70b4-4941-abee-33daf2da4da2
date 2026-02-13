<title>Relational Database Versioning and Temporal Design</title>
<url>https://bytedance.larkoffice.com/docx/SHv5duOILoaydIxKKi6cBzqXn5d</url>
<content>
## Introduction to Database Versioning
Designing a database schema that supports versioning, historical data, and rollbacks is a critical task for systems that require auditability, data analysis over time, or resilience against errors. A versioned schema allows you to answer not only "What is the data now?" but also "What was the data at a specific point in time?" and "How has this data changed?"

This document provides a comprehensive guide to designing and implementing versioning patterns in relational databases (RDBMS). It is intended for engineers and architects who need to build robust, auditable, and maintainable systems.

### Core Concepts
- **Immutability**: The core principle of versioning is that data is never truly deleted or overwritten. Instead, changes create new versions, preserving the old ones as historical records.

- **Temporality**: This refers to the time-based nature of data. We often distinguish between:
	- **Valid Time**: The time period during which a fact is true in the real world.
	- **Transaction Time**: The time period during which a fact is stored in the database.

- **Rollback**: The process of reverting data to a previous state. In a versioned system, this is typically a "soft" operation that creates a new version reflecting the old state, rather than a "hard" destructive operation.

---

## Design Patterns for Data Versioning
There are several established patterns for implementing versioning. The choice depends on factors like audit requirements, query complexity, write performance, and storage costs. Here is a high-level overview:

![board_EzgDwZ37QhxrQ6b4FbicYzdgnXT](board_EzgDwZ37QhxrQ6b4FbicYzdgnXT.drawio)

### 1. Append-Only with Effective Period (SCD Type 2)
This is one of the most common and intuitive patterns, often known as a "Slowly Changing Dimension" (Type 2) in data warehousing. Each record has an effective start and end date, defining the period during which it was the "current" version.

#### Design Principles
- A single table holds all versions of an entity.

- `effective_from` and `effective_to` (or similar) columns track the validity period.

- The "current" version is the one where `effective_to` is `NULL` or a far-future date (e.g., '9999-12-31').

- When an entity is updated, the `effective_to` of the current record is set to the current timestamp, and a new record is inserted with the updated data and a new `effective_from`.

#### When to Use
- You need a full, auditable history of changes.

- Point-in-time queries ("What did this look like last Tuesday?") are common.

- The number of writes is moderate compared to reads.

- Simplicity of implementation is valued.

#### Pros & Cons
<grid cols="2">
<column width="50">
  **<font color="green">Pros</font>:**
  - **Simple to understand and implement.**
  - **Full history in a single table.**
  - **Excellent for analytical and point-in-time queries.**
  - **Enforces immutability naturally.**
</column>
<column width="50">
  **<font color="red">Cons</font>:**
  - **Table can grow very large.**
  - **Queries for the "current" state are more complex (require&nbsp;WHERE effective_to IS NULL).**
  - **Updating requires two steps (closing old record, inserting new one), which should be transactional.**
  - **Referential integrity can be complex (more on this later).**
</column>
</grid>

#### Schema & SQL Example (PostgreSQL)
Here is a DDL for a `products` table using this pattern.

```sql
CREATE TABLE products (
    product_version_id BIGSERIAL PRIMARY KEY, -- A surrogate key for the version
    product_id BIGINT NOT NULL,              -- The stable identifier for the entity
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price NUMERIC(10, 2) NOT NULL,
    effective_from TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    effective_to TIMESTAMPTZ NOT NULL DEFAULT '9999-12-31',
    is_current BOOLEAN GENERATED ALWAYS AS (effective_to = '9999-12-31') STORED
);

-- Index for finding the current version of a product
CREATE INDEX idx_products_current ON products (product_id) WHERE is_current = TRUE;

-- Index for efficient point-in-time queries
CREATE INDEX idx_products_temporal ON products (product_id, effective_from, effective_to);

-- A view to simplify querying for the current state
CREATE VIEW products_current AS
SELECT *
FROM products
WHERE is_current = TRUE;
```

<callout icon="bulb" bgc="3" bc="3">
**Note:** The `is_current` generated column is a PostgreSQL feature that simplifies queries. For other databases, you would use `WHERE effective_to = '9999-12-31'` directly.
</callout>

#### Example Queries
**Point-in-Time Query:** Find the price of product `123` on `2023-01-15`.

```sql
SELECT price
FROM products
WHERE product_id = 123
  AND '2023-01-15'::TIMESTAMPTZ >= effective_from
  AND '2023-01-15'::TIMESTAMPTZ < effective_to;
```

**Diff Between Versions:** Compare versions `5` and `6` of product `123`.

```sql
SELECT
    v_old.name AS old_name, v_new.name AS new_name,
    v_old.price AS old_price, v_new.price AS new_price
FROM products AS v_old
JOIN products AS v_new ON v_old.product_id = v_new.product_id
WHERE v_old.product_version_id = 5
  AND v_new.product_version_id = 6;
```

#### Rollback Semantics
To roll back a change (e.g., revert from version 3 to version 2), you perform a **soft revert**:

1. Find the version you want to restore (version 2).

2. "Close" the current active version (version 3) by setting its `effective_to` to `NOW()`.

3. Insert a **new version** (version 4) that is a copy of the data from version 2, with `effective_from` set to `NOW()`.

The erroneous version 3 remains in the history, preserving the audit trail.

```sql
-- Assume product_id 123 was updated incorrectly (product_version_id = 3)
-- and we want to revert to the state of product_version_id = 2.

BEGIN;

-- 1. Close the current (bad) version
UPDATE products
SET effective_to = NOW()
WHERE product_id = 123 AND is_current = TRUE;

-- 2. Create a new version by copying the old, good one
INSERT INTO products (product_id, name, description, price, effective_from, effective_to)
SELECT
    product_id,
    name,
    description,
    price,
    NOW() AS effective_from,
    '9999-12-31' AS effective_to
FROM products
WHERE product_version_id = 2; -- The version we are restoring

COMMIT;
```

This preserves the entire history, including the mistake and its correction. This is a key principle of immutable data architectures. This lifecycle is visualized in the timeline below.

![board_MKGnwaqAKhjnFabdi2Vc8VaSnug](board_MKGnwaqAKhjnFabdi2Vc8VaSnug.drawio)

---

### 2. System-Versioned / Temporal Tables
Several modern databases (including PostgreSQL, SQL Server, and Oracle) have built-in support for temporal tables. This automates the process of creating and maintaining the history table, effectively implementing the append-only pattern at the database level.

#### Design Principles
- You define a table as `SYSTEM_VERSIONED`.

- The database automatically creates a hidden history table.

- When you `UPDATE` or `DELETE` rows in the main table, the database automatically copies the old version of the row into the history table with the correct time period.

- The main table always shows the current state, simplifying queries for current data.

- Special SQL syntax (`AS OF SYSTEM TIME`) is used to query historical data.

#### When to Use
- Your database supports it.

- You want the simplest possible query model for current data (`SELECT * FROM my_table`).

- You want the database to handle the versioning mechanism automatically and transactionally.

- Development speed and simplicity are high priorities.

#### Pros & Cons
<grid cols="2">
<column width="50">
  **<font color="green">Pros</font>:**
  - **Transparent to the application.** Standard DML statements (`UPDATE`, `DELETE`) work as expected.
  - **Extremely simple to query the current state.**
  - **Reduces application logic and potential for bugs.**
  - **Guaranteed transactional consistency.**
</column>
<column width="50">
  **<font color="red">Cons</font>:**
  - **Less portable across different RDBMS vendors.**
  - **Less control over the history table's structure (e.g., indexing, partitioning).**
  - **Can hide complexity, making it harder to debug performance issues.**
  - **Bitemporal modeling (valid time + transaction time) may not be fully supported.**
</column>
</grid>

#### Schema & SQL Example (PostgreSQL using `temporal_tables` extension)
This example uses a popular PostgreSQL extension. Native support is also being developed.

```sql
-- First, enable the extension
CREATE EXTENSION IF NOT EXISTS temporal_tables;

CREATE TABLE products_temporal (
    product_id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    sys_period TSTZRANGE NOT NULL
);

-- Turn this into a system-versioned table
CREATE TRIGGER versioning_trigger
BEFORE INSERT OR UPDATE OR DELETE ON products_temporal
FOR EACH ROW EXECUTE PROCEDURE versioning('sys_period', 'products_temporal_history', true);

-- The 'products_temporal_history' table is created and managed automatically.
```

#### Example Queries
**Point-in-Time Query:** Find the price of product `123` on `2023-01-15`.

```sql
SELECT price
FROM products_temporal_history
WHERE product_id = 123
  AND sys_period @> '2023-01-15'::TIMESTAMPTZ;

-- Or using the SQL:2011 standard syntax (if supported)
-- SELECT price
-- FROM products_temporal
-- FOR SYSTEM_TIME AS OF '2023-01-15'
-- WHERE product_id = 123;
```

#### Rollback Semantics
Rollback is conceptually similar to the manual append-only pattern but achieved with standard DML. To restore product `123` to its state on `2023-01-15`:

1. Query the history table to get the state of the product at that time.

2. `UPDATE` the main table with the retrieved historical data. This automatically creates a new history record for the state you are overwriting.

```sql
-- Get the old state
DECLARE old_name VARCHAR;
DECLARE old_price NUMERIC;
SELECT name, price INTO old_name, old_price
FROM products_temporal_history
WHERE product_id = 123
  AND sys_period @> '2023-01-15'::TIMESTAMPTZ;

-- Update the current record, which automatically archives the previous "current" state
UPDATE products_temporal
SET name = old_name, price = old_price
WHERE product_id = 123;
```

---

### 3. Versioned Entity with Latest Pointer
This pattern separates immutable versions from the "current" record pointer. It involves two tables: one to store all versions of an entity (which is append-only) and another to point to which version is the latest.

![board_De4hwZEfdhODt7bUrYhcBWlUnMh](board_De4hwZEfdhODt7bUrYhcBWlUnMh.drawio)

#### Design Principles
- A `_versions` table stores every version of an entity. This table is **immutable**; records are never updated. Each version has its own surrogate primary key (e.g., `version_id`).

- A "main" entity table (e.g., `products`) contains the stable ID and a foreign key pointing to the `version_id` of the current version.

- When an entity is updated, a new record is inserted into the `_versions` table, and the foreign key in the main table is updated to point to the new `version_id`.

#### When to Use
- Write performance is critical. Updating the "latest" pointer is a small, fast operation.

- You want to explicitly separate the concept of an "entity" from its "versions."

- Referential integrity is easier to manage, as other tables can foreign key to the stable `product_id`.

- You need to add metadata about the version itself (e.g., who made the change, why).

#### Pros & Cons
<grid cols="2">
<column width="50">
  **<font color="green">Pros</font>:**
  - **Fast writes.** Only a single row in the main table is updated.
  - **Clean separation of concerns.**
  - **Simplified referential integrity for related tables.**
  - **Easy to query the current state (a simple&nbsp;JOIN).**
  - **The&nbsp;_versions&nbsp;table can easily store version-specific metadata.**
</column>
<column width="50">
  **<font color="red">Cons</font>:**
  - **Requires a&nbsp;JOIN&nbsp;to get the full current record, which can be slightly slower than reading from a single table.**
  - **More complex transactional logic: you must insert the new version&nbsp;and&nbsp;update the pointer atomically.**
  - **Can lead to orphaned versions if the pointer update fails.**
</column>
</grid>

#### Schema & SQL Example (PostgreSQL)
```sql
CREATE TABLE product_versions (
    version_id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price NUMERIC(10, 2) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    author_id BIGINT -- Example of version-specific metadata
);

CREATE TABLE products (
    product_id BIGSERIAL PRIMARY KEY,
    current_version_id BIGINT NOT NULL,
    CONSTRAINT fk_current_version
        FOREIGN KEY(current_version_id)
        REFERENCES product_versions(version_id)
        DEFERRABLE INITIALLY IMMEDIATE
);

-- A view for convenience
CREATE VIEW products_current AS
SELECT
    p.product_id,
    pv.version_id,
    pv.name,
    pv.description,
    pv.price,
    pv.created_at
FROM products p
JOIN product_versions pv ON p.current_version_id = pv.version_id;
```

<callout icon="bulb" bgc="3" bc="3">
**Deferred Constraint:** The `DEFERRABLE` foreign key is a powerful feature. When creating a new product, you need to insert into `products` and `product_versions` at the same time, but one must come first. Deferring the constraint check to the end of the transaction allows you to do this.
</callout>

#### Example Update & Rollback
To update a product, you wrap the logic in a transaction.

```sql
BEGIN;

-- 1. Insert the new version and get its ID
INSERT INTO product_versions (name, price) VALUES ('New Awesome Gadget', 129.99)
RETURNING version_id INTO new_version_id;

-- 2. Update the main table to point to the new version
UPDATE products
SET current_version_id = new_version_id
WHERE product_id = 123;

COMMIT;
```

**Rollback** is extremely simple and safe with this pattern. To revert product `123` to a previous version (e.g., `version_id = 55`):

```sql
-- No new version is created, we just change the pointer.
-- This is a "hard" revert from the entity's perspective but "soft" for the system,
-- as the incorrect version is still preserved.
UPDATE products
SET current_version_id = 55
WHERE product_id = 123;
```

If you need to preserve the fact that a rollback **happened**, you would instead create a **new** version that copies the data from version `55` and point to that. This is the recommended approach for full auditability.

---

### 4. Audit / Ledger Tables
This pattern is less about versioning the entity itself and more about tracking changes to it. It involves a secondary table that logs every change as a discrete event.

#### Design Principles
- The main table (e.g., `products`) always holds the current state and is updated in place.

- An `audit_log` or `ledger` table stores a history of all transactions.

- Each entry in the audit table contains the entity ID, the old value, the new value, the timestamp of the change, and who made the change.

- This is typically implemented using database triggers (`AFTER UPDATE`, `AFTER DELETE`).

#### When to Use
- The primary requirement is a simple audit trail, not complex point-in-time queries.

- You need to keep the main table clean and optimized for reads of the current state.

- You want to capture the "before" and "after" state for each change explicitly.

- The logic can be fully encapsulated within the database using triggers.

#### Pros & Cons
<grid cols="2">
<column width="50">
  **<font color="green">Pros</font>:**
  - **Main table is very simple and fast for current-state queries.**
  - **Provides a clear, explicit log of what changed, when, and by whom.**
  - **Can be added non-intrusively to an existing schema.**
</column>
<column width="50">
  **<font color="red">Cons</font>:**
  - **Reconstructing the state of an entity at a specific point in time is very difficult and slow, requiring replaying the log.**
  - **The log table can grow extremely large.**
  - **Storing partial changes (e.g., as JSON blobs) can make querying the log difficult.**
  - **Business logic in triggers can be hard to manage, test, and version.**
</column>
</grid>

#### Schema & SQL Example (PostgreSQL)
```sql
CREATE TABLE products (
    product_id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);

CREATE TABLE products_audit_log (
    log_id BIGSERIAL PRIMARY KEY,
    product_id BIGINT NOT NULL,
    old_data JSONB,
    new_data JSONB,
    changed_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    changed_by VARCHAR(100)
);

-- Trigger function to capture changes
CREATE OR REPLACE FUNCTION log_product_changes()
RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'UPDATE') THEN
        INSERT INTO products_audit_log (product_id, old_data, new_data, changed_by)
        VALUES (OLD.product_id, to_jsonb(OLD), to_jsonb(NEW), current_user);
        RETURN NEW;
    ELSIF (TG_OP = 'DELETE') THEN
        INSERT INTO products_audit_log (product_id, old_data, changed_by)
        VALUES (OLD.product_id, to_jsonb(OLD), current_user);
        RETURN OLD;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER products_audit_trigger
AFTER UPDATE OR DELETE ON products
FOR EACH ROW EXECUTE FUNCTION log_product_changes();
```

#### Rollback Semantics
Rollback requires manually inspecting the log and applying a compensating change. To revert an incorrect price update on product `123`:

1. Find the relevant log entry.

2. Extract the `old_data` for the `price` field.

3. `UPDATE` the main `products` table with the old price. This action will itself be logged in the audit table, creating a complete trail of the error and the correction.

---

### 5. Event Sourcing
Event Sourcing is an advanced pattern where the state of an application is determined by a sequence of events. Instead of storing the current state, you store every single event that has ever happened in an append-only log.

#### Design Principles
- The "source of truth" is an `events` table that stores immutable events (e.g., `ProductCreated`, `PriceUpdated`, `ProductShipped`).

- The current state of an entity is derived by replaying all its events in order.

- To improve read performance, **projections** (materialized views or separate tables) are created from the event stream. These projections are optimized for specific query needs. For example, a `products_current_state` table can be built for fast lookups.

#### When to Use
- You have complex business logic and workflows.

- The "why" behind data changes is as important as the "what".

- You need to support many different views (projections) of the same data.

- In distributed systems (like microservices) where it can facilitate communication and data consistency.

#### Pros & Cons
<grid cols="2">
<column width="50">
  **<font color="green">Pros</font>:**
  - **The most complete and auditable history possible.**
  - **Captures intent, not just state changes.**
  - **Flexible reads through different projections.**
  - **Time travel is built-in; you can reconstruct state at any point.**
  - **Decouples write logic from read logic.**
</column>
<column width="50">
  **<font color="red">Cons</font>:**
  - **Significantly more complex to implement and manage.**
  - **Requires a messaging system or robust process for building projections.**
  - **"Eventual consistency" is a common characteristic, which may not be suitable for all applications.**
  - **Directly querying the event log for state is impractical.**
</column>
</grid>

#### Schema & SQL Example
The core is the `events` store. This is often not a traditional relational table but could be implemented as one.

```sql
CREATE TABLE events (
    event_id BIGSERIAL PRIMARY KEY,
    stream_id UUID NOT NULL, -- The ID of the entity (e.g., a product)
    event_type VARCHAR(100) NOT NULL,
    payload JSONB NOT NULL,
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    version INT NOT NULL
);

CREATE INDEX idx_events_stream ON events (stream_id, version);

-- A projection table for current product state
CREATE TABLE products_projection (
    product_id UUID PRIMARY KEY,
    name VARCHAR(255),
    price NUMERIC(10, 2),
    last_updated_at TIMESTAMPTZ
);
```

An application service would listen to the `events` stream and update `products_projection` accordingly.

#### Rollback Semantics
You never delete events. A rollback is achieved by emitting a **compensating event**. If a `PriceUpdated` event set the price incorrectly, you would publish a `PriceCorrection` event with the correct price. The system processes this new event, which updates the relevant projections to reflect the corrected state.

---

## Handling Referential Integrity
Versioning introduces complexity for foreign keys. When a `product` is versioned, what should an `order_item` reference?

#### Strategy 1: Foreign Key to the Stable ID
- **Description**: The `order_items` table has a `product_id` foreign key that references `products(product_id)`.

- **Behavior**: The order is always associated with the **entity**, not a specific version. If you look at an old order, it will appear to contain the **current** product details (name, price), which is usually incorrect.

- **When to use**: Almost never for transactional data like orders. It can be acceptable for non-critical relationships where the "current" view is always sufficient.

#### Strategy 2: Foreign Key to the Version ID
- **Description**: The `order_items` table has a `product_version_id` that references the primary key of the version table (e.g., `products(product_version_id)` in the append-only model, or `product_versions(version_id)` in the pointer model).

- **Behavior**: The order is permanently locked to the exact version of the product that was sold. This ensures historical accuracy.

- **When to use**: This is the correct approach for most transactional data (orders, invoices, etc.).

- **Challenge**: How do you find the `product_version_id` at the time of purchase? Your application logic must fetch the current version ID and store it.

#### Strategy 3: Denormalization / Caching
- **Description**: At the time of the transaction (e.g., when an order is placed), critical data from the parent entity is copied directly into the child table. For example, `order_items` would have its own `price` and `product_name` columns.

- **Behavior**: The `order_items` table becomes self-contained and immune to future changes in the `products` table. It's a snapshot of the data as it was.

- **When to use**: When historical accuracy is paramount and you want to avoid complex joins for historical reporting. Common in e-commerce and financial systems.

The best approach is typically a combination of **Strategy 2 and 3**: store the `product_version_id` for perfect traceability and denormalize the critical data (like price) to simplify business logic and reporting.

---

## Rollback Strategies In-Depth
While individual patterns have their rollback semantics, it's useful to formalize the strategies. The key is to balance auditability with operational ease.

![board_YHDtwnW5uhCsJYbYw3yc9wm6nte](board_YHDtwnW5uhCsJYbYw3yc9wm6nte.drawio)

#### 1. Soft Revert (Recommended)
- **How it works**: You create a **new version** that happens to contain the data of a previous, correct version. The erroneous version is not deleted; it simply becomes non-current.

- **Audit Trail**: This is the best approach for auditability. The history clearly shows: State A -> Mistake B -> Correction to State A (as a new version C).

- **Implementation**:
	- In the **Append-Only** pattern, you close the current record and insert a new one by copying an old one.
	- In the **Versioned Entity + Pointer** pattern, you can either create a new version record that's a copy of the old one, or for a simpler rollback, just update the pointer (a less auditable approach).

- **Trade-offs**: Slightly more storage, but preserves the entire history, which is invaluable for regulated industries or debugging complex business processes.

#### 2. Snapshot/Restore
- **How it works**: This is a database-level operation where a full or partial backup is restored. This is a "hard" revert.

- **Audit Trail**: The audit trail is lost. The database state reverts to a point in time as if the intervening period never happened.

- **Implementation**: Usually performed by a DBA. Not suitable for application-level logic.

- **Trade-offs**: High risk of data loss for all transactions that occurred after the snapshot was taken. Should only be used for catastrophic failures, not for correcting typical data entry errors.

#### 3. Transaction-Based Revert
- **How it works**: If you have a perfect, atomic log of every transaction (like in Event Sourcing, or a git-like commit log), you can create and apply a "revert" transaction that is the inverse of the original.

- **Audit Trail**: Perfect, as both the original transaction and the revert transaction are recorded.

- **Implementation**: Very complex. Requires the application to be designed around this concept from the ground up.

- **Trade-offs**: Extremely powerful but has a high implementation cost.

#### 4. Compensating Changes
- **How it works**: This is the business-level equivalent of a soft revert. Instead of thinking in terms of "reverting" data, you apply a new business operation that corrects the mistake.

- **Example**: If a user was billed incorrectly, you don't delete the invoice. You issue a credit note.

- **Implementation**: This is pure application logic. The database simply records the new compensating transaction.

- **Trade-offs**: This is the most robust and business-friendly approach, but it requires that your domain model includes these compensating actions.

<callout icon="bulb" bgc="5" bc="5">
**Key Takeaway:** For most application-level data correction, a **Soft Revert** or a **Compensating Change** is the correct strategy. Hard reverts via database restores are for disaster recovery only.
</callout>

---

## Performance, Storage, and Migration
#### Concurrency Control
When multiple users try to update the same record, you need to prevent lost updates.

- **Optimistic Locking**: Add a `version` number column to your main entity table. When you read a record to update it, you grab the current version number. The `UPDATE` statement then includes `WHERE id = ? AND version = ?`. If another process updated the record in the meantime, the version number won't match, the update will affect 0 rows, and your application can retry the transaction. This is a great fit for the **Versioned Entity + Pointer** pattern.

- **Write Fences**: For the **Append-Only** pattern, ensure that only one "current" version can exist for any given entity. This can be enforced with a partial index (`CREATE UNIQUE INDEX ... WHERE effective_to IS NULL`) or database constraints.

#### Performance & Storage
- **Indexing**: Temporal columns (`effective_from`, `effective_to`) and stable entity IDs (`product_id`) must be indexed. Composite indexes are often necessary for efficient point-in-time queries.

- **Partitioning**: For very large history tables, partitioning by date range (e.g., by year or month) on the `effective_from` or `created_at` column can dramatically improve query performance and simplify data management (e.g., archiving old data).

- **Archiving/Compression**: Historical data is often read-infrequently. You can move older partitions to slower, cheaper storage or use database features for table compression.

#### Migration Strategies
Adopting versioning in an existing, live database is a significant undertaking.

1. **Stop the World**: The simplest approach. Take the application offline, run a script to transform the schema and backfill history (if possible), and deploy the new application code. Only feasible for systems with low uptime requirements.

2. **Phased Migration with Triggers**:
	- Add the new versioning tables/columns to the database.
	- Create triggers on the original tables that populate the new versioning structures whenever a write occurs.
	- Run a background job to slowly backfill the history for existing records.
	- Once the new structures are fully populated and in sync, you can switch the application's read/write paths to use the new versioned schema and, eventually, decommission the old tables.

---

## Decision Framework & Anti-Patterns
#### How to Choose a Pattern?
<table col-widths="150,250,250,250">
    <tr>
        <td>**If you need...**</td>
        <td>**Primary Recommendation**</td>
        <td>**Secondary Option**</td>
        <td>**Reasoning**</td>
    </tr>
    <tr>
        <td>**Full, simple audit trail & analytics**</td>
        <td>Append-Only (SCD Type 2)</td>
        <td>Temporal Tables</td>
        <td>Best for point-in-time analysis. Temporal tables automate this.</td>
    </tr>
    <tr>
        <td>**High write performance & simple FKs**</td>
        <td>Versioned Entity + Pointer</td>
        <td>Audit/Ledger Tables</td>
        <td>Minimizes write contention and simplifies relationships to other tables.</td>
    </tr>
    <tr>
        <td>**Maximum simplicity & your DB supports it**</td>
        <td>Temporal Tables</td>
        <td>​-</td>
        <td>The database does all the heavy lifting.</td>
    </tr>
    <tr>
        <td>**To capture business intent & complex logic**</td>
        <td>Event Sourcing</td>
        <td>​-</td>
        <td>The only pattern that natively stores the "why" behind changes. High complexity.</td>
    </tr>
    <tr>
        <td>**A simple change log on an existing schema**</td>
        <td>Audit/Ledger Tables</td>
        <td>​-</td>
        <td>Least intrusive way to add basic change tracking.</td>
    </tr>
</table>

#### Anti-Patterns to Avoid
1. **Mutable History**: The biggest anti-pattern is allowing historical records to be updated. The history should be append-only.

2. **Using Timestamps for Versioning**: Relying on `updated_at` timestamps alone is not enough. Without a full record, you can't know what the data **was**. Timestamps are also not guaranteed to be unique, leading to race conditions.

3. **Ignoring Transactions**: All versioning operations that involve multiple steps (e.g., closing an old record and inserting a new one) must be wrapped in a database transaction to ensure atomicity.

4. **Complex Logic in Triggers**: While triggers are useful for simple audit logs, placing complex business logic in them makes the system hard to debug, test, and maintain. Keep triggers simple and focused.

5. **Forgetting about Indexes**: Versioned tables get large. Without proper indexing on temporal columns and entity IDs, query performance will grind to a halt.


</content>
