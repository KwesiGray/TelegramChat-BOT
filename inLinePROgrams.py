from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext, Updater, CallbackQueryHandler, ContextTypes
import constant as const

async def programs_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard =[
        [InlineKeyboardButton(text="Mining Engineering", callback_data="Agg:06-12")],
        [InlineKeyboardButton(text="Geomatic Engineering", callback_data="Agg:10-18")],
        [InlineKeyboardButton(text="Mineral Engineering", callback_data="Agg:11-18")],
        [InlineKeyboardButton(text="Petroleum Engineering", callback_data="Agg:06")],
        [InlineKeyboardButton(text="Geological Engineering", callback_data="Agg:11-14")],
        [InlineKeyboardButton(text="Environmental & Saftey Engineering", callback_data="Agg:12-18")],
        [InlineKeyboardButton(text="Mechanical Engineering", callback_data="Agg:08-10")],
        [InlineKeyboardButton(text="Electrical Engineering", callback_data="Agg:08-10")],
        [InlineKeyboardButton(text="Materials Engineering", callback_data="Agg:08-10")],
        [InlineKeyboardButton(text="Computer Science & Engineering", callback_data="Agg:08-10")],
        [InlineKeyboardButton(text="Mathematics", callback_data="Agg:10-18")],
        [InlineKeyboardButton(text="Renewable Energy Engineering", callback_data="Agg:09-12")],
        [InlineKeyboardButton(text="Information Technology", callback_data="Agg:11-14")],
        [InlineKeyboardButton(text="Petroleum Geoscience Engineering", callback_data="Agg:09")],     
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Select a Program to know Eligible Aggregates:', reply_markup=reply_markup)