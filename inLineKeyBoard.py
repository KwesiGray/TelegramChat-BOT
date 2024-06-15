from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler, CallbackContext, InlineQueryHandler, Updater, CallbackQueryHandler
import constant as const

async def faculty_buttons(update: Update, context: CallbackContext):
    """Presents a list of faculty buttons for user selection."""

    keyboard =[
        [InlineKeyboardButton(text="FMMT", callback_data=const.fmmt)],
        [InlineKeyboardButton(text="FOE", callback_data=const.foe)],
        [InlineKeyboardButton(text="FCMS", callback_data=const.fcms)],
        [InlineKeyboardButton(text="FGES", callback_data=const.fges)],
        [InlineKeyboardButton(text="SPeTs", callback_data=const.spets)],
        [InlineKeyboardButton(text="FIMS", callback_data=const.fims)]
    ]
    
    

    markup = InlineKeyboardMarkup(keyboard)
    

    await update.message.reply_text("Select a Faculty:", reply_markup=markup)
    
    
    
# write a function that will handle the callback data
async def handle_faculty_buttons(update: Update, context: CallbackContext):
    """Handle the callback data from the faculty buttons."""
    query = update.callback_query
    
    
    faculty = query.data
    faculty1 = query.data
    
    
    
    

    await query.answer(f"{faculty1}") # show the user that the bot is working on their request

    await query.message.reply_text(f"{faculty}") # send a reply to the user with the faculty they selected
    






# A function for the halls_ buttons 
async def halls_buttons(update: Update, context: CallbackContext):
    """Presents a list of halls buttons for user selection."""

    keyboard =[
        [InlineKeyboardButton(text="Chambers of Mines", callback_data=const.cmh)], 
        [InlineKeyboardButton(text="K.T", callback_data=const.kth)],
        [InlineKeyboardButton(text="Gold Refinery", callback_data=const.grh)]   
    ]
    
    markup = InlineKeyboardMarkup(keyboard)
    

    await update.message.reply_text("Select a Hall:", reply_markup=markup)


# write a function that will handle the callback data
async def handle_Halls_buttons(update: Update, context: CallbackContext):
    """Handle the callback data from the halls buttons."""
    query = update.callback_query
    
    Hall = query.data
   

    await query.answer(f"{Hall}") # show the user that the bot is working on their request
    await query.message.reply_text(f"{Hall} Hall") # send a reply to the user with the hall they selected






# A function for the programs buttons

async def programs_buttons(update: Update, context: CallbackContext):
    """Presents a list of programs buttons for user selection And to know thier eligible aggregates."""

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
    
    
    markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text("Select a Program to know Eligible Aggregates:", reply_markup=markup)