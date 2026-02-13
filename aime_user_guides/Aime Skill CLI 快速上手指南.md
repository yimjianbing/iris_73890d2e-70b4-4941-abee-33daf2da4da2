<title>Aime Skill CLI 快速上手指南</title>
<url>https://bytedance.larkoffice.com/wiki/UlgSwWSORiI0cFkqCcPcQ9GDnBc</url>
<content>
## 安装与准备
在开始使用前，请先完成 **CLI 的安装与认证**。

1. **安装 CLI**：打开终端，执行以下命令安装 `aime-skill-cli`。
```bash
npm install -g @byted/aime-skill-cli --registry=https://bnpm.byted.org --force
```

2. **登录认证**：安装成功后，执行登录命令。CLI 会自动打开浏览器引导你完成字节跳动 SSO 认证。
```bash
aime-skill-cli login
```
你也可以使用 `--qrcode` 参数通过二维码扫码登录。

## 快速开始
只需几步，即可完成一个 **Skill 的打包与上传**。

1. **打包 Skill**：进入你的项目目录，执行 `pack` 命令将 Skill 源码打包成 `.zip` 文件。`<skill_dir>` 是你的 Skill 源代码所在的目录。
```bash
aime-skill-cli pack <skill_dir>
```

![图片](img_RxU8bsmSOosfcSxpPRLcXA8Anfc.png)

1. **上传 Skill**：执行 `upload` 命令，上传刚刚生成的 `.zip` 文件。如果是首次操作，CLI 会引导你选择要上传到的 **Space**。
```bash
aime-skill-cli upload <path/to/skill.zip>
```

![图片](img_MiQ6bymz5oCJaLxtOgfcD0PAnoc.png)

1. **查看列表**：上传成功后，可以通过 `list` 命令查看当前 Space 下的所有 Skill，确认上传结果。
```bash
aime-skill-cli list
```

![图片](img_EornbPG8voMvXsxWrCwcHWNhn0b.png)

## 常用命令
- `update <skill_name>`：通过指定新的 `.zip` 文件来更新一个已有的 Skill。
```bash
aime-skill-cli update <skill_name> -f <path/to/new_skill.zip>
```

- `delete <skill_name>`：从 Space 中删除一个 Skill。
```bash
aime-skill-cli delete <skill_name>
```

![图片](img_SCPObLz65om7OmxRewucwGXFnnf.png)

- `enable <skill_name>` / `disable <skill_name>`：在 Space 中启用或禁用一个 Skill。
```bash
aime-skill-cli disable <skill_name>
```

## 高级用法
你可以通过配置文件或环境变量来自定义 CLI 的行为，例如**永久切换 Space** 或**指定私有化部署环境**。

- **设置默认 Space ID**：如果你需要频繁操作某个固定的 Space，可以将其 ID 设置为默认值，避免重复选择。
```bash
aime-skill-cli config set space_id <your_space_id>
```

- **设置 Base URL**：如果你的目标环境是 i18n 的 AIME，你需要将 `base_url` 指向对应的服务地址: https://aime.tiktok-row.net/
```bash
aime-skill-cli config set base_url <your_aime_base_url>
```

- **查看配置**：使用 `config list` 可以查看所有已设置的配置项。
```bash
aime-skill-cli config list
```

## 常见问题与提示
1. **命令执行失败并提示认证错误怎么办？**这通常是因为登录凭证已过期。请重新执行 `aime-skill-cli login` 即可。

2. **如何向指定 Space 上传 Skill？**除了通过 `config set space_id` 设置全局默认值外，你也可以在执行 `upload`、`list` 等命令时通过 `--space-id <space_id>` 参数临时指定本次操作的目标 Space。

3. **如何打包 Skill 的不同版本（变体）？**你可以在 Skill 源码根目录创建一个 `hooks.json` 文件来定义不同的变体。然后在使用 `pack` 命令时，通过 `-v <variant_name>` 参数打包指定变体，或使用 `-a` 参数打包所有已定义的变体。

4. **配置文件保存在哪里？**CLI 的配置文件默认保存在用户主目录下的 `~/.aime-skill-cli/config.json` 文件中。


</content>
