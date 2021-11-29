import utils.imageProcessing as imageP

from skimage import io

from telegram import Update
from telegram.ext import CallbackContext


def pull_image_handler(update: Update, context: CallbackContext) -> None:
    path = "custom/file.jpg"
    with open(path, 'wb') as f:
        context.bot.get_file(update.message.document).download(out=f)

    image = imageP.start(path)
    # file_id = update.message.photo[-1].file_id
    # newFile = context.bot.getFile(file_id)
    #
    # image = io.imread(newFile['file_path'])
    #
    # image = imageP.start(image)
    # update.message.reply_photo(
    #     photo=image,
    #     caption="ok"
    # )
