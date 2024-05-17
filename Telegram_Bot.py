# All the Libraries needed for this project
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


TOKEN: Final = 'YOUR BOT TOKEN GOES HERE'
BOT_USERNAME : Final = '@CTSL_Bot' # Your BOT USERNAME & should start with the @ symbol


#Commands the user can intereact with on telegram
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Welcome To The CTSL WORK Assistant Bot")
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Welcome To The Help Desk of CTSL")
  
  