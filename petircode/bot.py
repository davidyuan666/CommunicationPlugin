"""
Core bot functionality
"""
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

from .config import config
from .handlers.commands import claude_command

logger = logging.getLogger(__name__)


class PetriBot:
    """Main bot class"""

    def __init__(self):
        """Initialize the bot"""
        self.application = None

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        user = update.effective_user
        await update.message.reply_text(
            f"Hello {user.first_name}! 👋\n\n"
            "I'm PetriCode bot - A simple Telegram message bridge.\n"
            "I receive messages and forward tasks to Claude Code CLI.\n\n"
            "Use /help to see available commands."
        )

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        help_text = """
可用命令:

/start - 启动机器人
/help - 显示帮助信息
/info - 获取机器人信息
/claude <操作> - 使用Claude Code CLI执行操作

示例:
• /claude 搜索 Claude 3.5 Sonnet 相关信息
• /claude 列出当前目录的文件
• /claude 帮我分析这段代码

发送任何消息，我会回复你！
"""
        await update.message.reply_text(help_text)

    async def info_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /info command"""
        info_text = (
            "🤖 PetriCode Bot v0.2.0\n\n"
            "A simple Telegram message bridge.\n"
            "Receives messages and forwards tasks to Claude Code CLI."
        )
        await update.message.reply_text(info_text)

    async def echo_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Echo received messages"""
        text = update.message.text
        await update.message.reply_text(f"You said: {text}")

    def setup_handlers(self):
        """Setup command and message handlers"""
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("info", self.info_command))
        self.application.add_handler(CommandHandler("claude", claude_command))
        self.application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self.echo_message)
        )

    def run(self):
        """Run the bot"""
        config.validate()
        self.application = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()
        self.setup_handlers()
        logger.info("Starting PetriCode bot...")
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)
