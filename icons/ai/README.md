# AI 模型资源包的图标

本目录里的图标文件会显示为 AI 模型资源包里各角色的图标。某个文件缺失时，对应角色回退显示自绘的简化徽记。

## 文件要求

- 格式：`.svg` 或 `.png`（先找 `.svg`，没有再找 `.png`）。
- 文件名必须与下表完全一致，全小写。
- 建议用正方形、背景透明的图。图片会等比缩放后居中放在白色圆角方块上。
- PNG 建议边长 128 像素以上，角色在出场动画里会被放大。

## 文件名对照

| 角色 | 文件 |
|---|---|
| ChatGPT | `openai.svg` |
| Claude | `claude.svg` |
| Gemini | `gemini.svg` |
| Grok | `grok.svg` |
| DeepSeek | `deepseek.svg` |
| 通义千问 | `qwen.png` |
| 豆包 | `doubao.svg` |
| Kimi | `kimi.svg` |
| Llama | `llama.svg` |
| Copilot | `copilot.svg` |

要增加角色，需要同时在 `index.html` 的 `PACKS.ai` 列表里加一项，并在这里放入对应文件。

## 关于商标

这些图标是各公司的商标，使用时请遵守各公司的品牌使用条款。
