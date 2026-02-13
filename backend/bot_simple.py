"""
AdBounty Telegram Bot - Versão com python-telegram-bot
"""

import os
import logging
import asyncio
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token from environment
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set")

# ============================================================================
# Command Handlers
# ============================================================================

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    keyboard = [[
        InlineKeyboardButton("📱 Open AdBounty", url="https://adbounty.app")
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🎯 Welcome to AdBounty!\n\n"
        "The decentralized ad marketplace for Telegram channels.\n\n"
        "Advertisers: Create bounties and reach verified channels\n"
        "Channel Owners: Earn TON by posting ads\n\n"
        "Use /help to see available commands.",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    help_text = """
🆘 AdBounty Help

📖 Available Commands:
/start - Start the bot
/help - Show this help message
/my - View your bounties and deals

🔗 Links:
- Website: https://adbounty.app
- Support: @adbounty_support
"""
    await update.message.reply_text(help_text)

async def my_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show user's info"""
    user = update.effective_user
    await update.message.reply_text(
        f"👤 Your Info:\n\n"
        f"ID: {user.id}\n"
        f"Name: {user.full_name}\n"
        f"Username: @{user.username}\n\n"
        f"More features coming soon!"
    )

# ============================================================================
# Error handler
# ============================================================================

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors"""
    logger.error(f"Update {update} caused error {context.error}")

# ============================================================================
# Main function
# ============================================================================

def main():
    """Start the bot"""
    logger.info("AdBounty Bot starting with python-telegram-bot...")
    
    # Create application
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("my", my_command))
    
    # Add error handler
    app.add_error_handler(error_handler)
    
    # Start bot
    logger.info("Bot is polling...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
