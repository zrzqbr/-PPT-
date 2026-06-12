# 贡献指南

感谢你对本项目的关注！欢迎通过 Issue 和 Pull Request 参与贡献。

## 提交 Issue

### Bug 报告

请包含以下信息：

- 使用的 Python 版本和操作系统
- 输入文件类型（HTML / .pptx）
- 完整的错误信息或截图
- 预期行为 vs 实际行为

### 功能建议

请说明：

- 你想解决的具体问题
- 期望的实现方式
- 是否愿意提交 PR 实现

## 提交 Pull Request

### 流程

1. Fork 本仓库
2. 创建功能分支：`git checkout -b feature/your-feature`
3. 提交修改：`git commit -m "feat: add your feature"`
4. 推送分支：`git push origin feature/your-feature`
5. 创建 Pull Request，描述清楚改动内容和原因

### Commit Message 规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 格式：

| 前缀 | 用途 | 示例 |
|------|------|------|
| `feat:` | 新功能 | `feat: add JSON to PPTX converter` |
| `fix:` | 修复 Bug | `fix: correct font size overflow on slide 3` |
| `docs:` | 文档变更 | `docs: update README quick start` |
| `chore:` | 项目维护 | `chore: update requirements.txt` |
| `refactor:` | 重构代码 | `refactor: extract common color utils` |

### 代码风格

- Python 代码遵循 [PEP 8](https://peps.python.org/pep-0008/)
- 函数和类必须有 docstring
- 变量命名使用 snake_case

## 品牌资产修改禁区

以下文件受品牌规范约束，**不可随意修改**：

| 文件 / 目录 | 说明 |
|-------------|------|
| `assets/backgrounds/` | 品牌背景图（长沙城市线稿） |
| `assets/logos/` | 腾讯云架构师同盟 Logo |
| `assets/fonts/` | TencentSans 字体文件 |
| `assets/templates/` | 基准模板 .pptx |
| `references/brand-rules.md` | 品牌配色/排版硬规范 |

如需修改以上内容，请先提交 Issue 说明理由，经讨论通过后再提交 PR。

## 测试

提交 PR 前请确保测试通过：

```bash
python scripts/test_v5.py
python scripts/verify_output.py your-output.pptx
```

## 许可

提交贡献即表示你同意将代码以 [MIT License](./LICENSE) 授权发布。
