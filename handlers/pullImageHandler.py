import os
import utils.imageProcessing as imageP

from telegram import Update
from telegram.ext import CallbackContext


def pull_image_handler(update: Update, context: CallbackContext) -> None:
    path = "custom/file.jpg"

    if not os.path.exists("./custom"):
        os.makedirs("./custom")

    with open(path, 'wb') as f:
        context.bot.get_file(update.message.document).download(out=f)

    image = imageP.start(path)

    update.message.reply_photo(
        photo=image,
        caption="ok"
    )
