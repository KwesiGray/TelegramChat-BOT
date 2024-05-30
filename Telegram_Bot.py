# All the Libraries needed for this project
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


TOKEN: Final = '7447252101:AAGooCzgQN38B0E18HrEkKrtdOcuMIZYrmA'
BOT_USERNAME : Final = '@CTSL_Tadi_BOT' # Your BOT USERNAME & should start with the @ symbol


#Commands the user can intereact with on telegram
#So commands with thier respective responses
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Welcome To The CTSL WORK Assistant Bot")
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Welcome To The Help Desk of CTSL")
  
async def website_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    """ Visit The Official Website of CTSL: https://ctslafrica.com/
    """
    )


#This is the main function that handles the responses of the bot to the user
from sklearn.feature_extraction.text import CountVectorizer # Import CountVectorizer from sklearn library to convert text data into numerical data
from sklearn.naive_bayes import MultinomialNB # Import MultinomialNB from sklearn library to train a Naive Bayes classifier

# Your training data: a list of sentences and a list of responses. 
# The sentences are the input data and the responses are the output data and each sentence has a corresponding response(mapped to each other)
sentences = ["hello", "how are you", "i am also doing good", "what's your name", "i need some help", "Thank You"]
responses = ["Hi There!!. Type the /help Command For Help.", "I am Doing Good Please. You?", "That's Very Good To Hear. Type The /help Command for Help", "Your Can Call Me Breslin Your Bot Assistant. For Help?? Type /help.", "I am here...Type the /help command for me to help!", "You Are Highly Welcome"]

# Vectorize your training data
vectorizer = CountVectorizer() # Create an instance of the CountVectorizer class
X_train = vectorizer.fit_transform(sentences) # Convert the sentences into numerical data using the fit_transform method

# Train a Naive Bayes classifier
clf = MultinomialNB() # Create an instance of the MultinomialNB class
clf.fit(X_train, responses) # Train the classifier using the fit method with the input data and output data

# Now you can predict responses to new sentences
def handle_response(text: str) -> str: # Define a function that takes a string as input and returns a string as output
    X_test = vectorizer.transform([text]) # Convert the input text into numerical data using the transform method
    response = clf.predict(X_test) # Predict the response using the predict method with the numerical data as input
    return response[0]     # Return the predicted response as output



async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE): # Define a function that takes an update and context as input and returns a response
    message_type: str = update.message.chat.type  # Get the type of the chat from the update
    text: str = update.message.text  # Get the text message from the update 
    response: str = ""   # Initialize response
    
    print(f'User: ({update.message.chat.id}) in {message_type}: "{text}"') # Print the user ID, chat type, and text message
    
     #Check if text is None or an empty string
    if not text: # Check if the text is None or an empty string
        print("Received a message without text") # Print a message indicating that a message without text was received
        return # Return None

    
    if message_type == "group":
        if BOT_USERNAME in text: 
            new_text : str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
               
    print("BOT: ", response)
    await update.message.reply_text(response) 
    
    
  
  
  
  
  
  
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update: {update} caused this error {context.error}")



if __name__ == "__main__": # Check if the script is being run directly
    print ("Starting ChatBot.....") # Print a message indicating that the chatbot is starting
    # Create the Application and pass it your bot's token.
    app = Application.builder().token(TOKEN).build()
    
    
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("website", website_command))
    
    
    
     #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))



    #ERRORS
    app.add_error_handler(error)



    #Polls the bot
    print("polling..")
    app.run_polling(poll_interval =2)