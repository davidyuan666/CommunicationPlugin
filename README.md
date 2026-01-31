# CommunicationPlugin

简单的 Telegram 消息桥接机器人。

## 功能特性

- **消息接收**: 接收来自 Telegram 的消息
- **消息推送**: 推送结果到 Telegram App
- **Claude Code CLI 集成**: 将任务转发给 Claude Code CLI 处理

## 设计理念

本项目专注于消息的接收和推送，不包含任何业务逻辑：
- ✅ 接收 Telegram 消息
- ✅ 推送消息到 Telegram
- ✅ 调用 Claude Code CLI 执行任务
- ❌ 不包含搜索功能
- ❌ 不包含 AI 对话功能
- ❌ 不包含数据处理逻辑

所有业务逻辑（搜索、分析、处理等）都由 Claude Code CLI 或其他第三方工具完成。

## 快速开始

1. 安装依赖:
```bash
pip install -r requirements.txt
```

2. 配置环境变量（复制.env.example为.env并填写）:
```
TELEGRAM_BOT_TOKEN=your_bot_token
CLAUDE_WORK_DIR=C:\workspace\claudecodelabspace
```

3. 运行机器人:
```bash
python -m petircode.main
```

## 命令列表

- `/start` - 启动机器人
- `/help` - 显示帮助信息
- `/info` - 获取机器人信息
- `/claude <操作>` - 使用 Claude Code CLI 执行操作

## 使用示例

```
/claude 搜索 Claude 3.5 Sonnet 相关信息
/claude 列出当前目录的文件
/claude 帮我分析这段代码
```

机器人会将任务转发给 Claude Code CLI，并将结果推送回 Telegram。
