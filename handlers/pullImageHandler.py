from skimage import io
import matplotlib.pyplot as plt

from telegram import Update
from telegram.ext import CallbackContext


def pull_image_handler(update: Update, context: CallbackContext) -> None:
    file_id = update.message.photo[-1].file_id
    newFile = context.bot.getFile(file_id)

    image = io.imread(newFile['file_path'])

    plt.imshow(image)
    plt.show()

    update.message.reply_markdown_v2(
        fr'Photo ok'
    )
