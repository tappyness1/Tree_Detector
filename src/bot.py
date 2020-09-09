from src.inference import load_image, classifier
from telegram.ext import Updater, MessageHandler, Filters
import os
from functools import partial

def classify_image(bot, update, util):
    image_file = bot.getFile(update.message.photo[-1].file_id)
    image_file.download("image.jpg")
    pred, prob = classifier("image.jpg")
    update.message.reply_markdown(pred)

def main():
    TOKEN = os.getenv("TOKEN")

    updater = Updater(TOKEN)
    dp = updater.dispatcher

    util = utils.Utils()
    classify_image_callback = partial(classify_image, util=util)

    dp.add_handler(MessageHandler(Filters.photo, classify_image_callback))

    PORT = int(os.environ.get("PORT", "5000"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))


if __name__ == '__main__':
    main()