from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler, CallbackContext, InlineQueryHandler, Updater, CallbackQueryHandler
import constant as const




async def faculty_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
      [InlineKeyboardButton(text="FMMT", callback_data=const.fmmt)],
        [InlineKeyboardButton(text="FOE", callback_data=const.foe)],
        [InlineKeyboardButton(text="FCMS", callback_data=const.fcms)],
        [InlineKeyboardButton(text="FGES", callback_data=const.fges)],
        [InlineKeyboardButton(text="SPeTs", callback_data=const.spets)],
        [InlineKeyboardButton(text="FIMS", callback_data=const.fims)]
    ]
    
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Select a Faculty to Know the Departments Under it:', reply_markup=reply_markup)
    

async def handle_faculty_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    callback_data = query.data
    await query.answer(callback_data)
    #await query.edit_message_text(const.faculties_command)
    await query.message.reply_text(text="Selected Option: {}".format(callback_data))
    
    
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


# The buttons for Information on the faculties
async def info_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard1 = [
      [InlineKeyboardButton(text="FMMT", callback_data=const.fmmt)],
        [InlineKeyboardButton(text="FOE", callback_data=const.foe)],
        [InlineKeyboardButton(text="FCMS", callback_data=const.fcms)],
        [InlineKeyboardButton(text="FGES", callback_data=const.fges)],
        [InlineKeyboardButton(text="SPeTs", callback_data=const.spets)],
        [InlineKeyboardButton(text="FIMS", callback_data=const.fims)]
    ]
    
    
    reply_markup1 = InlineKeyboardMarkup(keyboard1)
    await update.message.reply_text('Select a Faculty to have more INFORMATION about it:', reply_markup=reply_markup1)
    



async def handle_info_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query1 = update.callback_query
    callback_data1 = query1.data
    await query1.answer(callback_data1)
    #await query1.edit_message_text(const.faculties_command)
    await query1.message.reply_text(text="Selected The: {}".format(callback_data1))
    
    
    if callback_data1 == const.fmmt:
        await query1.message.reply_text(const.fmmt_info)
    elif callback_data1 == const.foe:
        await query1.message.reply_text(const.foe_info)
    elif callback_data1 == const.fcms:
        await query1.message.reply_text(const.fcms_info)
    elif callback_data1 == const.fges:
        await query1.message.reply_text(const.fges_info)
    elif callback_data1 == const.spets:
        await query1.message.reply_text(const.spets_info)
    elif callback_data1 == const.fims:
        await query1.message.reply_text(const.fims_info)
