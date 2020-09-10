from inference import load_image, classifier
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import os
from functools import partial

def classify_image(bot, update):
    """[summary]

    Args:
        bot ([type]): [description]
        update ([type]): [description]
    """
    image_file = bot.getFile(update.message.photo[-1].file_id)
    image_file.download("image.jpg")
    pred, prob = classifier("image.jpg")
    update.message.reply_markdown(pred)

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

# def help(update, context):
#     """Send a message when the command /help is issued."""
#     update.message.reply_text('Help!')

# def echo(update, context):
#     """Echo the user message."""
#     update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    TOKEN = os.getenv("TOKEN")

    updater = Updater(token = TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error) 
    
    classify_image_callback = partial(classify_image)
    dp.add_handler(MessageHandler(Filters.photo, classify_image_callback))

    PORT = int(os.environ.get("PORT", "8443"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
    updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))
    
    updater.idle()


if __name__ == '__main__':
    main()