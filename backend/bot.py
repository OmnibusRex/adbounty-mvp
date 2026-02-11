"""
AdBounty Telegram Bot
Handles automatic posting of ads to channels and user notifications
"""

import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import httpx

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot token from environment
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set")

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ============================================================================
# States for FSM
# ============================================================================

class BountyStates(StatesGroup):
    waiting_for_amount = State()
    waiting_for_text = State()
    waiting_for_link = State()
    waiting_for_channels = State()

# ============================================================================
# Command Handlers
# ============================================================================

@dp.message(Command("start"))
async def start_command(message: Message):
    """Handle /start command"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📱 Open AdBounty", web_app={"url": "https://adbounty.app"})],
        [InlineKeyboardButton(text="📚 Help", callback_data="help")]
    ])
    
    await message.answer(
        "🎯 Welcome to AdBounty!\n\n"
        "The decentralized ad marketplace for Telegram channels.\n\n"
        "Advertisers: Create bounties and reach verified channels\n"
        "Channel Owners: Earn TON by posting ads\n\n"
        "Tap the button below to get started!",
        reply_markup=keyboard
    )

@dp.message(Command("help"))
async def help_command(message: Message):
    """Handle /help command"""
    help_text = """
🆘 AdBounty Help

📖 How it works:
1. Advertisers create bounties with TON payment
2. Channel owners bid on bounties
3. Ads are posted to channels automatically
4. Owners confirm views and receive payout

💰 For Advertisers:
- Create bounties with target channels
- Pay in TON via smart contract
- Track posting status in real-time

💵 For Channel Owners:
- Browse available bounties
- Accept bids and earn TON
- Confirm views to release payout

🔗 Links:
- Website: https://adbounty.app
- Docs: https://docs.adbounty.app
- Support: @adbounty_support
"""
    await message.answer(help_text)

@dp.message(Command("mybounties"))
async def my_bounties_command(message: Message):
    """Show user's bounties"""
    user_id = message.from_user.id
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BACKEND_URL}/bounties/user/{user_id}")
            
            if response.status_code == 200:
                data = response.json()
                bounties = data.get("bounties", [])
                
                if not bounties:
                    await message.answer("You don't have any bounties yet. Create one to get started!")
                    return
                
                text = "📊 Your Bounties:\n\n"
                for bounty in bounties:
                    text += f"💰 {bounty['ton_amount']} TON\n"
                    text += f"Status: {bounty['status']}\n"
                    text += f"Deadline: {bounty['deadline']}\n\n"
                
                await message.answer(text)
            else:
                await message.answer("Error fetching bounties. Please try again.")
    except Exception as e:
        logger.error(f"Error in my_bounties: {str(e)}")
        await message.answer("An error occurred. Please try again later.")

@dp.message(Command("deals"))
async def my_deals_command(message: Message):
    """Show user's active deals"""
    user_id = message.from_user.id
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BACKEND_URL}/deals/user/{user_id}")
            
            if response.status_code == 200:
                data = response.json()
                deals = data.get("deals", [])
                
                if not deals:
                    await message.answer("You don't have any active deals yet.")
                    return
                
                text = "📋 Your Active Deals:\n\n"
                for deal in deals:
                    text += f"📢 {deal['bounty_title']}\n"
                    text += f"💰 {deal['amount']} TON\n"
                    text += f"Status: {deal['status']}\n\n"
                
                await message.answer(text)
            else:
                await message.answer("Error fetching deals. Please try again.")
    except Exception as e:
        logger.error(f"Error in my_deals: {str(e)}")
        await message.answer("An error occurred. Please try again later.")

# ============================================================================
# Callback Query Handlers
# ============================================================================

@dp.callback_query(lambda c: c.data == "help")
async def help_callback(callback_query: types.CallbackQuery):
    """Handle help button callback"""
    await callback_query.answer()
    await help_command(callback_query.message)

# ============================================================================
# Bot Functions (called from backend)
# ============================================================================

async def send_ad_to_channel(channel_id: int, ad_text: str, ad_link: str, advertiser_id: int):
    """Send ad message to a channel"""
    try:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔗 Visit", url=ad_link)]
        ])
        
        message = await bot.send_message(
            chat_id=channel_id,
            text=f"📢 {ad_text}\n\n🔗 Learn more via the link below.",
            reply_markup=keyboard
        )
        
        logger.info(f"Ad posted to channel {channel_id}")
        return {
            "status": "success",
            "message_id": message.message_id,
            "channel_id": channel_id
        }
    except Exception as e:
        logger.error(f"Error posting ad to channel {channel_id}: {str(e)}")
        return {
            "status": "error",
            "error": str(e)
        }

async def notify_user(user_id: int, message_text: str):
    """Send notification to user"""
    try:
        await bot.send_message(chat_id=user_id, text=message_text)
        logger.info(f"Notification sent to user {user_id}")
        return {"status": "success"}
    except Exception as e:
        logger.error(f"Error notifying user {user_id}: {str(e)}")
        return {"status": "error", "error": str(e)}

async def notify_payout(user_id: int, amount: float, bounty_id: str):
    """Notify user about payout"""
    message = f"""
✅ Payout Released!

💰 Amount: {amount} TON
📊 Bounty ID: {bounty_id}

Your earnings have been transferred to your wallet.
"""
    return await notify_user(user_id, message)

# ============================================================================
# Main function
# ============================================================================

async def main():
    """Start the bot"""
    logger.info("AdBounty Bot starting...")
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
