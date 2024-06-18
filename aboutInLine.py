from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler, CallbackContext, InlineQueryHandler, Updater, CallbackQueryHandler

# Assuming constant.py exists with the defined constants
from constant import mission, vision, coreValues, mission_St, vision_St, coreValues_St

# Assuming the following functions are defined in your code

async def About_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("mission", callback_data=mission)],  # Use constants directly
        [InlineKeyboardButton("vision", callback_data=vision)],
        [InlineKeyboardButton("Core Values", callback_data=coreValues)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Select an Option to know more about UMaT:', reply_markup=reply_markup)

async def handle_About_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        query = update.callback_query
        callback_data = query.data
        await query.answer()

        if callback_data == mission:
            await query.message.reply_text(mission_St)
        elif callback_data == vision:
            await query.message.reply_text(vision_St)
        elif callback_data == coreValues:
            await query.message.reply_text(coreValues_St)

    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the error gracefully (e.g., send an error message to the user)

# ... rest of your Telegram bot code (including token initialization)