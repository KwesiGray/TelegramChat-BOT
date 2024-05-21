# All the Libraries needed for this project
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


TOKEN: Final = 'YOUR BOT TOKEN GOES HERE'
BOT_USERNAME : Final = '@CTSL_Bot' # Your BOT USERNAME & should start with the @ symbol


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
clf = MultinomialNB()
clf.fit(X_train, responses)

# Now you can predict responses to new sentences
def handle_respon(text: str) -> str: # Define a function that takes a string as input and returns a string as output
    X_test = vectorizer.transform([text]) # Convert the input text into numerical data using the transform method
    response = clf.predict(X_test)
    return response[0] 