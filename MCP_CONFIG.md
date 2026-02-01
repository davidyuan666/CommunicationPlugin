# MCP 配置指南

本文档说明如何在 Claude Code CLI 中配置 Telegram Sender MCP 服务器。

## 项目说明

本项目是一个标准 MCP 服务器，为 Claude Code CLI 提供 Telegram 消息收发能力。

### MCP Server (`sender_server.py`)

**功能**:
- `send_telegram_message`: 发送消息到 Telegram
- `get_telegram_updates`: 获取 Telegram 最近的消息

**使用场景**: 在 Claude Code CLI 中执行命令，通过 MCP 工具与 Telegram 交互

---

## 配置步骤

### 第一步：设置环境变量

创建 `.env` 文件（或设置系统环境变量）：

```bash
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

**获取 Bot Token**:
1. 在 Telegram 中找到 @BotFather
2. 发送 `/newbot` 创建新机器人
3. 按提示设置机器人名称和用户名
4. 复制获得的 Token

### 第二步：安装依赖

```bash
cd TelegramSenderMCP
pip install -r requirements.txt
```

### 第三步：配置 Claude Code CLI

编辑 Claude Code CLI 的配置文件。配置文件位置：
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Linux: `~/.config/Claude/claude_desktop_config.json`

添加以下配置：

```json
{
  "mcpServers": {
    "telegram-sender": {
      "command": "python",
      "args": [
        "C:\\workspace\\claudecodelabspace\\TelegramSenderMCP\\sender_server.py"
      ],
      "env": {
        "TELEGRAM_BOT_TOKEN": "your_bot_token_here"
      }
    }
  }
}
```

**注意**:
- 将路径替换为你的实际路径
- 将 `your_bot_token_here` 替换为你的实际 Bot Token
- Windows 路径使用双反斜杠 `\\`

---

## 使用方法

启动 Claude Code CLI 后，可以使用以下工具：

**发送消息**:
```
Send a message "Hello from Claude!" to Telegram chat ID 123456789
```

**获取最近消息**:
```
Get recent Telegram messages
```

---

## 测试

运行测试脚本验证配置：

```bash
cd TelegramSenderMCP
python test_bot.py
```

这将测试：
- Bot 连接是否正常
- 是否能获取 Bot 信息
- 是否能获取最近的消息

---

## 故障排查

### 问题：MCP Server 无法启动

**检查**:
1. 确认 Python 版本 >= 3.10
2. 确认已安装所有依赖：`pip install -r requirements.txt`
3. 确认环境变量 `TELEGRAM_BOT_TOKEN` 已设置
4. 查看 Claude Code CLI 日志

### 问题：无法发送消息

**检查**:
1. Bot Token 是否正确
2. Chat ID 是否正确（可以通过 `get_telegram_updates` 获取）
3. 机器人是否有发送消息的权限

### 问题：无法获取消息

**检查**:
1. 是否已向机器人发送过消息
2. Bot Token 是否正确
3. 网络连接是否正常

---

## 安全建议

1. **不要将 Bot Token 提交到 Git 仓库**
   - 使用 `.env` 文件存储 Token
   - 确保 `.env` 在 `.gitignore` 中

2. **定期更换 Bot Token**
   - 如果 Token 泄露，立即通过 @BotFather 重新生成

3. **限制机器人权限**
   - 只授予必要的权限
   - 考虑使用白名单限制可以使用机器人的用户

---

## 相关文档

- [README.md](README.md) - 项目概述
- [SETUP.md](SETUP.md) - 快速启动指南
- [MCP 官方文档](https://modelcontextprotocol.io/)
