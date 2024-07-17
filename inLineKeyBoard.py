from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler, CallbackContext, InlineQueryHandler, Updater, CallbackQueryHandler
import constant as const




async def faculty_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
      [InlineKeyboardButton(text="FMMT ", callback_data=const.fmmt)],
        [InlineKeyboardButton(text="FOE ", callback_data=const.foe)],
        [InlineKeyboardButton(text="FCMS ", callback_data=const.fcms)],
        [InlineKeyboardButton(text="FGES ", callback_data=const.fges)],
        [InlineKeyboardButton(text="SPeTs ", callback_data=const.spets)],
        [InlineKeyboardButton(text="FIMS ", callback_data=const.fims)]
    ]
    
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text='Select a Faculty to Know the Departments Under it:', reply_markup=reply_markup)
    

async def handle_faculty_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    callback_data = query.data
    await query.answer()
    
    #await query.edit_message_text(const.faculties_command)
    #await query.message.reply_text((text="David")+text="Selected Option: {}".format(callback_data))
    await query.message.reply_text("{}".format(callback_data))
    
    
    if callback_data == const.fmmt:
        await query.message.reply_text(const.fmmt_programs)
    elif callback_data == const.foe:
        await query.message.reply_text(const.foe_programs)
    elif callback_data == const.fcms:
        await query.message.reply_text(const.fcms_programs)
    elif callback_data == const.fges:
        await query.message.reply_text(const.fges_programs)
    elif callback_data == const.spets:
        await query.message.reply_text(const.spets_programs)
    elif callback_data == const.fims:
        await query.message.reply_text(const.fims_programs)


        await query.message.reply_text(text="For More Info on the Departments, Tap the /info_ Command Or better still tap the /faculties_ command to know the respective faculties and their Departments.")







async def about_buttons(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton(text="Mission", callback_data="/Mission")],
        [InlineKeyboardButton(text="Vision", callback_data="/Vision")],
        [InlineKeyboardButton(text="Core Values", callback_data="/Core_Values")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Select an Option to know more about UMaT:', reply_markup=reply_markup)
     



async def handle_about_buttons(update: Update, context: CallbackContext):
    query = update.callback_query
    callback_data = query.data
    await query.answer()
    await query.message.reply_text("{}".format(callback_data))
    

    if callback_data == "/Mission":
        await query.message.reply_text(const.Mission)
    elif callback_data == "/Vision":
        await query.message.reply_text(const.Vision)
    elif callback_data == "/Core_Values":
        await query.message.reply_text(const.Core_Values)

  