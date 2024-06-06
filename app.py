import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
import requests

# Set up logging here.......
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the handler for the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Howdy! Your Movie wiki here. Type 'hello' to get a greeting!")

# Define the handler for user messages
def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text.lower()
    if user_message == 'hello':
        update.message.reply_text("Hello! This bot can serve as a movie wiki. Search by typing any movie name. Btw, my favourite director is Christopher Nolan")
    elif user_message:
        # Call the OMDb API
        api_key = 'XXX'  #YOUR_API_KEY_HERE
        url = f'http://www.omdbapi.com/?apikey={api_key}&t={user_message}'
      
        response = requests.get(url)
        data = response.json()

        if data.get('Response') == 'True':
            title = data.get('Title')
            year = data.get('Released')
            plot = data.get('Plot')
            dir = data.get('Director')
            poster = data.get('Poster')
            update.message.reply_text(f"{title} ({year}):\nDirector: {dir}\nPlot: {plot}\n{poster}\n")
        else:
            update.message.reply_text("Movie not found. Please check the title and try again.")
    else:
        update.message.reply_text("Please provide a movie title.")




###################-----------------Below CODE is used for the Telegram BOT

def main() -> None:

    updater = Updater(token='YYY', use_context=True)  #YOUR_TELEGRAM_BOT_TOKEN_HERE
    dispatcher = updater.dispatcher

    # Add handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(None, handle_message))  # No Filters argument

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
