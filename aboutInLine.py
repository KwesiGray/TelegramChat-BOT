from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler, CallbackContext, InlineQueryHandler, Updater, CallbackQueryHandler
import constant as const



async def About_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(text="Mission", callback_data=const.Mission)],
        [InlineKeyboardButton(text="Vision", callback_data=const.Vision)],
        [InlineKeyboardButton(text="Core Values", callback_data=const.CoreValues)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Select an Option to know more about UMaT:', reply_markup=reply_markup)
    
    query = update.callback_query
    callback_data = query.data
    
    if callback_data == const.Mission:
        await query.message.reply_text(const.Mission_St)