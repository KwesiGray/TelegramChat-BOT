import os
import logging
import constant as const
import inLineKeyBoard as line
import inLinePROgrams as prog
from typing import Final
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler, CallbackContext, InlineQueryHandler, Updater, CallbackQueryHandler, ConversationHandler
from httpx import ConnectTimeout
from dotenv import load_dotenv, dotenv_values

load_dotenv()

bot_token = os.getenv("Bot_Token")
bot = Bot(token=bot_token)
BOT_USERNAME : Final = '@UMAT_TARKWA_bot'



# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Stages
START_ROUTES, END_ROUTES = range(2)
# Callback data
ONE, TWO, THREE, FOUR = range(4)





#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE)-> str:
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).k
    
            
    keyboard = [
        [
            InlineKeyboardButton("Fresher", callback_data="/start"),
            InlineKeyboardButton("Non-Fresher", callback_data="Quit"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard  
    
    await update.message.reply_text("Hello!! 'Breslin' here Welcome. To The UMaT Admissions Assistant Bot. I am here to help you with all your admission queries. Please Choose a Route to get started", reply_markup=reply_markup)
    
  
    
    #await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return START_ROUTES
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(const.help_command)


async def faculties_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(const.faculties_command)


async def programs_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(const.programs_command)


async def eligibility_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(const.eligibility_command)


async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(const.contact_command)



async def website_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(const.website_command)



async def halls_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(const.halls_command)


# function for the in_depth command
async def in_depth_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(const.in_depth_command)


async def mission_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(const.Mission)


async def vision_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(const.Vision)

async def core_values_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(const.Core_Values)







# #RESPONSES
# #def handle_response(text: str)->str:
#    # processed: str = text.lower()

#     if "hello" in processed:
#         return "hi there how may i help you"

#     if "how are you" in processed:
#         return "I am Doing Good Please. You?"

#     if "i am also doing good" in processed or "i am also fine" in processed:
#         return "That's Very Good To Hear. How May I Help You?"

#     if "what's your name" in processed or "name" in processed:
#         return "Your Can Call Me Breslin Your Bot Assistant"

#     if "i need some help" in processed or "help" in processed:
#         return "I am here...Type the /help command for me to help!"

#     return "Please come agian ...I am not PROGRAMMED for That"








from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Your training data: a list of sentences and a list of responses.
sentences = const.sentences
responses = const.responses

#sentences = ["What halls are available", "What courses are available", "What are the faculties", "What are the eligibility criteria", "What is the contact information", "What is the website link"]
#responses = ["K.T Hall & Chambers Of Mines Hall (CMH) & Gold Refinery Hall (GRH)", "(Computer Science & Engineering) & (Mechanical Engineering) & (Mining Engineering)& (Environmental & Saftey Engineering)", "FOE & FMMT & SPET & FGES", "Agg: 12 - Agg: 08 - Agg: 06", "Hot line: +233 3121 97734"]

# Vectorize your training data
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(sentences)

# Train a Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train, responses)

# Now you can predict responses to new sentences
def handle_respon(text: str) -> str:
    X_test = vectorizer.transform([text])
    response = clf.predict(X_test)
    return response[0]








async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type # Get the type of the chat from the update
    text: str = update.message.text # Get the text message from the update
    response: str = ""  # Initialize response

    print(f'User: ({update.message.chat.id}) in {message_type}: "{text}"')


    if not text: # Check if the text is None or an empty string
        print("Received a message without text") # Print a message indicating that a message without text was received
        return # Return None


    if message_type == "group": # checks if the message is from a group
        if BOT_USERNAME in text: # checks if the bot username is in the message
            new_text : str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_respon(new_text)
        else:
            return
    else:
        response: str = handle_respon(text)

    print("BOT: ", response)
    await update.message.reply_text(response)







async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update: {update} caused this error {context.error}")





if __name__ == "__main__": # Check if the script is being run directly
    print ("Starting ChatBot.....")
    # Create the Application and pass it your bot's token.
    app = Application.builder().token(bot_token).build()


    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("faculties", faculties_command))
    app.add_handler(CommandHandler("programs", programs_command))
    app.add_handler(CommandHandler("eligibility", eligibility_command))
    app.add_handler(CommandHandler("contact", contact_command))
    app.add_handler(CommandHandler("website", website_command))
    app.add_handler(CommandHandler("halls", halls_command))
    app.add_handler(CommandHandler("mission", mission_command))
    app.add_handler(CommandHandler("vision", vision_command))
    app.add_handler(CommandHandler("core_values", core_values_command))







    # For The Buttons in (in_depth)command list
    app.add_handler(CommandHandler("in_depth", in_depth_command)) # how to add a command to the bot after creating the command function








    # For The Buttons in (faculties)command list
    app.add_handler(CommandHandler("faculties_", line.faculty_buttons))

    # To handle the callbacks for the faculty buttons
    app.add_handler(CallbackQueryHandler(line.handle_faculty_buttons))


    # For The Buttons in (Halls)command list
    # app.add_handler(CommandHandler("halls_", line.halls_buttons))
    # app.add_handler(CallbackQueryHandler(line.handle_Halls_buttons))


    # For The Buttons in (programs)command list
    app.add_handler(CommandHandler("programs_", prog.programs_buttons))
    #app.add_handler(CallbackQueryHandler(line.handle_programs_buttons))


    # FOR THE ABOUT SECTION
    app.add_handler(CommandHandler("about", line.about_buttons))

    app.add_handler(CallbackQueryHandler(line.handle_about_buttons))












    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))




    #ERRORS
    app.add_error_handler(error)



    #Polls the bot
    print("Polling.....")
    app.run_polling(poll_interval =3)






