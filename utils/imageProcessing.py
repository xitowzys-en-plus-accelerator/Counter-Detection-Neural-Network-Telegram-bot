import cv2 as cv
import numpy
import numpy as np

from io import BytesIO


def numpy_to_binary(arr):
    is_success, buffer = cv.imencode(".jpg", arr)
    io_buf = BytesIO(buffer)
    return io_buf.read()


def start(image: numpy.ndarray) -> bytes:
    """
    Handling the sent image by the user and sending it back to the user

    :param image: image in numpy array
    :return: binary image
    """
    image_invert = np.invert(image)
    return numpy_to_binary(image_invert)
