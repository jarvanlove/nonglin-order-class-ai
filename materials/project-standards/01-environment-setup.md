# 01 - 环境安装指南

> 目标：确保每台学生电脑都能运行 Claude Code CLI、Trae-CN、Python 后端和 PostgreSQL。

---

## 1. Node.js（v20.x LTS 或更高）

### 安装步骤
1. 运行讲师提供的 Node.js 安装包（`node-v20.x.x-x64.msi`）
2. 一路点击"Next"，保持默认选项
3. 安装完成后，打开 PowerShell 或 Git Bash，运行：

```bash
node --version
npm --version
```

应输出 `v20.x.x` 和 `10.x.x` 以上。

### 安装 pnpm（可选但推荐）
```bash
npm install -g pnpm
pnpm --version
```

---

## 2. Git（v2.40+）

### 安装步骤
1. 运行讲师提供的 Git 安装包（`Git-2.x.x-64-bit.exe`）
2. 安装选项保持默认即可
3. 验证：

```bash
git --version
```

---

## 3. Python（v3.10+）

### 安装步骤
1. 运行讲师提供的 Python 安装包（`python-3.10.x-amd64.exe`）
2. **关键**：勾选 "Add Python to PATH"
3. 验证：

```bash
python --version
pip --version
```

### 安装 Python 虚拟环境工具
```bash
pip install virtualenv
```

---

## 4. PostgreSQL（v15+）

### 安装步骤
1. 运行讲师提供的 PostgreSQL 安装包（`postgresql-15.x-x64.exe`）
2. 安装过程中设置密码（建议统一设置为 `student123`，方便教学）
3. 保持默认端口 `5432`
4. 安装完成后，打开 "pgAdmin 4"（开始菜单中搜索）
5. 连接本地服务器，创建一个测试数据库：

```sql
CREATE DATABASE test_db;
```

### 验证安装
```bash
psql --version
```

---

## 5. Claude Code CLI

### 安装步骤
1. 确保 Node.js 已安装完成
2. 打开 PowerShell 或 Git Bash，运行：

```bash
npm install -g @anthropic-ai/claude-code
```

3. 验证安装：

```bash
claude --version
```

### 首次配置
1. 运行 `claude`
2. 按提示输入 API Key（由讲师统一提供）
3. 选择默认模型（建议 `claude-sonnet-4`）

---

## 6. Trae-CN

### 安装步骤
1. 访问 [Trae 官网](https://www.trae.ai/) 下载安装包
2. 或使用讲师提供的离线安装包
3. 安装完成后，用手机号或邮箱注册登录
4. 在设置中启用 Builder Mode

---

## 7. 一键验证脚本

将以下内容保存为 `check-env.py`，运行即可检测所有环境：

```python
import subprocess
import sys

def check(cmd, name):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {name}: {result.stdout.strip()}")
            return True
        else:
            print(f"❌ {name}: 未安装或配置错误")
            return False
    except Exception as e:
        print(f"❌ {name}: 检查失败 - {e}")
        return False

all_ok = True
all_ok &= check("node --version", "Node.js")
all_ok &= check("npm --version", "npm")
all_ok &= check("git --version", "Git")
all_ok &= check("python --version", "Python")
all_ok &= check("pip --version", "pip")
all_ok &= check("psql --version", "PostgreSQL")
all_ok &= check("claude --version", "Claude Code CLI")

if all_ok:
    print("\n🎉 所有环境已就绪！")
else:
    print("\n⚠️ 部分环境未安装，请参考上文安装。")
    sys.exit(1)
```

运行方式：
```bash
python check-env.py
```

---

## 8. 常见问题

| 问题 | 解决方案 |
|------|---------|
| `node` 命令找不到 | 重新安装 Node.js，确保勾选 "Add to PATH" |
| `python` 命令找不到 | 手动添加 Python 安装目录到系统 PATH |
| PostgreSQL 连接失败 | 检查服务是否运行（Windows 服务中找 `postgresql-x64-15`） |
| Claude Code CLI 安装慢 | 换 npm 镜像：`npm config set registry https://registry.npmmirror.com` |
| 端口 5432 被占用 | 查找占用进程并关闭，或修改 PostgreSQL 端口 |
