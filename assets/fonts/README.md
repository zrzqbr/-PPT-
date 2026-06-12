# 字体说明

本 Skill 已内置腾讯体字体文件（TTF 格式），位于本目录：

| 文件 | 说明 |
| --- | --- |
| `TencentSans-W3.ttf` | 腾讯体 W3 常规体（正文用） |
| `TencentSans-W7.ttf` | 腾讯体 W7 粗体（标题用） |

## 版权声明

> **TencentSans 字体版权归深圳市腾讯计算机系统有限公司所有。**
>
> 本项目引用该字体仅用于腾讯云架构师技术同盟沙龙的 PPT 品牌适配技术演示。
> 如需将本字体用于其他商业用途，请遵循腾讯官方字体授权协议。
> 字体下载及授权详情请参考：https://tecdn.qq.com/tdesign/download/brand/TencentSans.zip

## 必须使用的字体名（family name）

在生成 PPT 时，**只能使用以下两个 family name**，不要用其他写法：

- `TencentSans W3`（正文，中间一个空格）
- `TencentSans W7`（标题，中间一个空格）

## 不要使用的写法

| 错误写法 | 原因 |
| --- | --- |
| `腾讯体 W3` / `腾讯体 W7` | 中文别名，仅在中文版 Office 识别，跨平台容易显示为空白方块 |
| `TencentSansW3` / `TencentSansW7` | PostScript 名（无空格），PowerPoint 不直接识别 |
| `TTTGB Medium` / `Helvetica` / `PingFang SC` | 不同字体，违反字体规范 |

## 安装方法

### Windows（用户级，无需管理员）

```powershell
# 把字体文件复制到用户字体目录
$src = "<skill-dir>\assets\fonts"
$dst = "$env:LOCALAPPDATA\Microsoft\Windows\Fonts"
Copy-Item "$src\TencentSans-W3.ttf" $dst -Force
Copy-Item "$src\TencentSans-W7.ttf" $dst -Force

# 注册到注册表（让 Office 立即识别）
$regPath = "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Fonts"
New-ItemProperty -Path $regPath -Name "TencentSans W3 (TrueType)" `
    -Value "$dst\TencentSans-W3.ttf" -PropertyType String -Force
New-ItemProperty -Path $regPath -Name "TencentSans W7 (TrueType)" `
    -Value "$dst\TencentSans-W7.ttf" -PropertyType String -Force
```

### Windows（系统级）

把 `TencentSans-W3.ttf` 和 `TencentSans-W7.ttf` 复制到 `C:\Windows\Fonts\`（需管理员）。

### macOS

把字体文件复制到 `~/Library/Fonts/`（用户级）或 `/Library/Fonts/`（系统级）。

### Linux（含 LibreOffice 渲染服务器）

```bash
mkdir -p ~/.fonts
cp TencentSans-W3.ttf TencentSans-W7.ttf ~/.fonts/
fc-cache -fv
```

## 安装后验证

安装完成后**重启 PowerPoint / WPS / Office 进程**，在字体下拉框搜索 `TencentSans` 应能看到两个字体。

如果 LibreOffice 转换 PDF 时字体仍显示成空白方块，重启 LibreOffice 进程：

```bash
pkill soffice
soffice --headless --convert-to pdf input.pptx
```
