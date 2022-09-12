#  OCR :  optical character recognition
#  Dependencies  : Pillow, OpenCV, pytesseract, numpy

import cv2
from PIL import Image
import pytesseract
import numpy as np
from Preprocessing import PreProcessing



test_image = "test.png"
test_image2 = "test2.png"
no_noise = 'temp/no_noise.jpg'
img_equation = 'temp/equation.png'


def load_picture(image_source) -> print:
    """Returns information about the image"""
    im = Image.open(image_source)
    return print(im)

def parse_string_from_image(image_source) -> str:
    ocr_result = pytesseract.image_to_string(image_source)
    return ocr_result



if __name__ == "__main__":

    # Parse text from image OCR
    #print(parse_string_from_image(img_equation))

    load_picture(img_equation)

    # # Converted to gray scale
    # gray = convert_grayscale(test_image2)
    # # Convert to binary
    # gray_binary = THRESH_BINARY(gray)
    # Removed noise from image
    # Picture1 = PreProcessing(test_image2)
    # # Dilated image
    # dilate_image = Picture1.thick_font()
    # # Eroded image
    # eroded_image = Picture1.thin_font()



