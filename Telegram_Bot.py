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
  
async def website_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    """ Visit The Official Website of CTSL: https://ctslafrica.com/
    """
    )



from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Your training data: a list of sentences and a list of responses.
sentences = ["hello", "how are you", "i am also doing good", "what's your name", "i need some help", "Thank You"]
responses = ["Hi There!!. Type the /help Command For Help.", "I am Doing Good Please. You?", "That's Very Good To Hear. Type The /help Command for Help", "Your Can Call Me Breslin Your Bot Assistant. For Help?? Type /help.", "I am here...Type the /help command for me to help!", "You Are Highly Welcome"]

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