from typing import Final
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


TOKEN: Final = '717mat1122307:zAFv0APwm232afsuUghH7TfUkcanzPgJpuloops'
BOT_USERNAME : Final = '@CTSL_Bot'


#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Welcome To The CTSL WORK Assistant Bot")
  