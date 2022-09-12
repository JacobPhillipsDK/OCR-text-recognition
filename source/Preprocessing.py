import cv2
import numpy as np


class PreProcessing:
    def __init__(self, image, shouldPrintInfo = False):
        self.shouldPrintInfo = shouldPrintInfo
        self.source_image = cv2.imread(image)
        self.run()

    def run(self):
        print("Running operation on image")
        grayscale = self.convert_grayscale_and_threshold()
        no_noise = self.noise_removal()
        self.write_image(f'grayscale', grayscale)
        self.write_image(f'no_noise', no_noise)
        return print("Successfully did the preprocessing")

    def convert_grayscale_and_threshold(self):
        """Convert the Image to grayscale with a given source image returns black and white image used with a threshold, change number to adapt to different images"""
        if self.shouldPrintInfo:
            print("Converting Image to grayscale")
        image = cv2.cvtColor(self.source_image, cv2.COLOR_BGR2GRAY)
        thresh, im_bw = cv2.threshold(image, 210, 230, cv2.THRESH_BINARY)
        return im_bw

    def noise_removal(self):
        """Removing Noise with Dilate and erode and then with medianblur"""
        if self.shouldPrintInfo:
            print("Removing Noise from picture")
        image_source = self.convert_grayscale_and_threshold()
        kernel = np.ones((1, 1), np.uint8)
        image_source = cv2.dilate(image_source, kernel, iterations=1)
        kernel = np.ones((1, 1), np.uint8)
        image_source = cv2.erode(image_source, kernel, iterations=1)
        image_source = cv2.morphologyEx(image_source, cv2.MORPH_CLOSE, kernel)
        image_source = cv2.medianBlur(image_source, 3)
        return image_source

    def write_image(self, name, image_source, showimage=False):
        if showimage:
            cv2.imshow(f'{name}', image_source)
        cv2.imwrite(f'temp/{name}.jpg', image_source)
        cv2.waitKey(0)


    def bounding_box(self):
        if self.shouldPrintInfo:
            print("Creating bounding box")


    #### Experiment ####

    ## Change the font size with Dilation and Erosion

    def thin_font(self):
        """Erosion"""
        image = cv2.bitwise_not(self.noise_removal())  # Revert the image ( white and black -> black and white )
        kernel = np.ones((2, 2), np.uint8)  # Higher array size harder to see the font -> Smaller it gets
        image = cv2.erode(image, kernel, iterations=1)
        # Convert image back from bitwise
        image = cv2.bitwise_not(image)
        self.write_image("Thin font", image)
        return image

    def thick_font(self):
        """Dilate"""
        image = cv2.bitwise_not(self.noise_removal())  # Revert the image ( white and black -> black and white )
        kernel = np.ones((2, 2), np.uint8)  # Higher array size harder to see the font -> Smaller it gets
        image = cv2.dilate(image, kernel, iterations=1)
        # Convert image back from bitwise
        image = cv2.bitwise_not(image)
        self.write_image("thick_font", image)
        return image
