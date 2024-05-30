from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler


TOKEN: Final = '7170598307:AAGXai5Vl8qVlCef1HtvbSeJsP7lL1xL8aY'
BOT_USERNAME : Final = '@UMAT_TARKWA_bot'

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!! 'Breslin' here Welcome To The UMaT Admissions Assistant Bot. Type the /help Command For any Assistance regarding UMaT Admissions.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    """
/start->

/help-> Here's Your Help Command

/faculties-> Faculties in UMaT(Tarkwa)

/courses-> Courses in UMaT(Tarkwa)

/halls-> Halls of Residence(Tarkwa)

/eligibility-> Aggregates Allowed in UMaT

/contact-> Contact INFO of UMaT

/website-> School Website link

    """
    )



async def faculties_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    """These Are The Faculties Available :
    -> FOE
    -> FMMT
    -> SPET
    -> FGES
    """
    )


async def courses_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    """These Are The Courses Available :

    -> Computer Science & Engineering
    -> Mechanical Engineering
    -> Mining Engineering
    -> Environmental & Saftey Engineering

    """
    )


async def eligibility_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    """These Are The Eligigble Aggregates Available To Enroll Here:

    -> Agg: 15
    -> Agg: 12
    -> Agg: 08
    -> Agg: 06
    """
    )


async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
""" Contact Details:

- Hot line: +233 3121 97734

- The Registrar : registrar@umat.edu.gh

- The WebMaster : webmaster@umat.edu.gh

- Postal: Box 237, Tarkwa. W/R
 """
    )

async def website_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    """ Visit The Official Website of The School Here : https://umat.edu.gh/
    """
    )



async def halls_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
"""These Are The Halls of Residence Available:
-K.T Hall

-Chambers Of Mines Hall (CMH)

-Gold Refinery Hall (GRH)
"""
    )


#RESPONSES
#def handle_response(text: str)->str:
   # processed: str = text.lower()

    if "hello" in processed:
        return "hi there how may i help you"

    if "how are you" in processed:
        return "I am Doing Good Please. You?"

    if "i am also doing good" in processed or "i am also fine" in processed:
        return "That's Very Good To Hear. How May I Help You?"

    if "what's your name" in processed or "name" in processed:
        return "Your Can Call Me Breslin Your Bot Assistant"

    if "i need some help" in processed or "help" in processed:
        return "I am here...Type the /help command for me to help!"

    return "Please come agian ...I am not PROGRAMMED for That"








from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Your training data: a list of sentences and a list of responses.
sentences = ["hello", "how are you", "i am also doing good", "what's your name", "i need some help", "Thank You", "Breslin"]
responses = ["Hi There!!. Tap the /help Command For Help.", "I am doing great. How are you doing yourself?", "That's very good to hear. Tap the /help Command for help", "You can call me Breslin Your Bot Assistant. For Help?? Tap /help.", "I am here...Tap the /help command for me to help!", "Anytime!.", "Hello There!...Here for INFO? Tap /help."]

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






if __name__ == "__main__":
    print ("Starting ChatBot.....")
    # Create the Application and pass it your bot's token.
    app = Application.builder().token(TOKEN).build()


    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(CommandHandler("faculties", faculties_command))
    app.add_handler(CommandHandler("courses", courses_command))
    app.add_handler(CommandHandler("eligibility", eligibility_command))
    app.add_handler(CommandHandler("contact", contact_command))
    app.add_handler(CommandHandler("website", website_command))
    app.add_handler(CommandHandler("halls", halls_command))





    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))



    #ERRORS
    app.add_error_handler(error)



    #Polls the bot
    print("polling..")
    app.run_polling(poll_interval =2)





