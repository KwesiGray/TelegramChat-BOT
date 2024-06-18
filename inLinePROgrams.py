from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext, Updater, CallbackQueryHandler

programs = [
    "Mining Engineering",
    "Geomatic Engineering",
    "Mineral Engineering",
    "Petroleum Engineering",
    "Electrical & Electronics Engineering",
    "Logistics Engineering",
    "CyberSecurity", 
    "Geological Engineering",
    "Environmental & Saftey Engineering",
    "Mechanical Engineering",
    "Materials Engineering",
    "Computer Science & Engineering",
    "Mathematics",
    "Renewable Energy Engineering",
    "Information Technology",
    "Petroleum Geoscience Engineering",
]

aggregates = [
    "08-12",
    "11-18",
    "11-16",
    "06",
    "08-10",
    "11-14",
    "12-18",
    "10-12",
    "08-10",
    "08-10",
    "08-10",
    "08-10",
    "10-18",
    "09-12",
    "11-14",
    "09-11",
]

# Combine programs and aggregates into a list of tuples
programs_with_aggregates = list(zip(programs, aggregates))

async def programs_buttons(update: Update, context: CallbackContext) -> None:
    keyboard = []
    for program, aggregate in programs_with_aggregates:
        callback_data = f"Agg:{aggregate}"
        keyboard.append([InlineKeyboardButton(text=program, callback_data=callback_data)])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Select a Program to know Eligible Aggregates:', reply_markup=reply_markup)

async def handle_program_button(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    # Extract the aggregate from the callback data
    _, aggregate = query.data.split(":")
    
    # Send the aggregate as a reply
    await query.message.reply_text(f'The allowed aggregate is: {aggregate}')

# Assuming you have an Updater instance named updater
