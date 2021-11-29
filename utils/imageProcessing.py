import cv2 as cv
from PIL import Image
import numpy as np

from io import BytesIO


def numpy_to_binary(arr):
    is_success, buffer = cv.imencode(".jpg", arr)
    io_buf = BytesIO(buffer)
    return io_buf.read()


def start(path) -> bytes:
    """
    Handling the sent image by the user and sending it back to the user

    :param image: image in numpy array
    :return: binary image
    """
    img = Image.open(path)
    image = np.array(img)

    image_invert = np.invert(image)

    return numpy_to_binary(image_invert)
