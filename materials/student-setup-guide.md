# 农林高校AI工具实训课程 · 学生环境安装指南

> 本指南为课前准备清单。请在课程开始前 1 天完成全部安装与验证。

---

## 一、必须安装的软件（按顺序）

| 序号 | 软件 | 版本要求 | 下载地址 | 验证命令/方式 | 用途 |
|------|------|----------|----------|---------------|------|
| 1 | **Trae IDE** | 最新版 | https://trae.cn | 打开后能看到 Builder / Chat / Solo 三个入口 | AI 原生 IDE，课程核心编码工具 |
| 2 | **Node.js** | LTS 20.x 及以上 | https://nodejs.org | `node -v` 输出 v20.x.x | 前端项目运行环境 |
| 3 | **Python** | 3.10 及以上 | https://python.org | `python --version` | 数据处理、轻量后端脚本 |
| 4 | **Git** | 2.40 及以上 | https://git-scm.com | `git --version` | 版本控制、代码提交 |
| 5 | **Chrome 或 Edge** | 最新版 | 系统自带或官网 | 打开开发者工具（F12）正常 | 浏览器调试、网页预览 |
| 6 | **WorkBuddy** | 最新版 | https://workbuddycn.com | 安装后桌面右下角出现图标，能正常唤起 | AI 桌面助手，本地文件处理与自动化 |
| 7 | **QClaw** | 最新版 | https://qclaw.qq.com | 微信扫码绑定成功，能进入对话界面 | 腾讯 AI Agent，信息收集与自动化 |

---

## 二、安装后必做验证（5 分钟）

1. **Trae 登录**：使用手机号或邮箱注册并登录，确保 Builder 模式可用。
2. **QClaw 绑定微信**：扫码后确认能在手机端收到 QClaw 消息推送。
3. **WorkBuddy 授权**：首次打开时允许文件系统访问权限，测试一次“批量重命名”功能。
4. **Node.js 国内镜像（可选但推荐）**：
   ```bash
   npm config set registry https://registry.npmmirror.com
   ```
5. **Git 配置身份**：
   ```bash
   git config --global user.name "你的姓名"
   git config --global user.email "你的邮箱"
   ```

---

## 三、不需要安装的软件（避免冲突）

以下软件**不要**在本课程中安装或使用，以免与课程工具链冲突或造成不必要的复杂度：

| 软件 | 原因 |
|------|------|
| MySQL / PostgreSQL | 课程使用 SQLite（Python 内置），无需额外数据库服务 |
| Docker / Kubernetes | 超出课程范围，本地环境已足够 |
| VS Code + Copilot 插件 | 课程统一使用 Trae，避免 IDE 切换导致的操作差异 |
| Cursor / Windsurf | 与 Trae 功能重叠，课程演示均以 Trae 为准 |
| Anaconda（完整版） | 体积过大，课程仅需基础 Python，如需环境管理可使用 Miniconda |
| 虚拟机 / 双系统 | 本机 Windows / macOS 直接安装即可，无需虚拟化层 |

---

## 四、常见问题速查

| 现象 | 解决方案 |
|------|----------|
| Trae Builder 模式无法使用 | 检查网络连接，Trae 部分功能需联网；确认已登录账号 |
| `node` 命令找不到 | 安装时未勾选 "Add to PATH"，重新安装或手动添加环境变量 |
| QClaw 微信绑定失败 | 确认微信为最新版；尝试切换网络（校园网可能限制） |
| WorkBuddy 无法读取桌面文件 | 检查系统权限设置（Windows：设置 > 隐私 > 文件系统；macOS：安全性与隐私 > 文件和文件夹） |
| Git 提交时提示身份未配置 | 执行上方“Git 配置身份”命令 |

---

## 五、课前提交检查

完成安装后，在课程群回复以下格式：

```
【环境就绪】
- 操作系统：Windows 11 / macOS 14 / 其他
- Trae：已登录
- Node.js：v20.x.x
- Python：3.10.x
- Git：已配置
- QClaw：微信已绑定
- WorkBuddy：已授权
```

> 若任一环节失败，提前在群里 @助教，避免开课当天占用课堂时间。
