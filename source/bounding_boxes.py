import cv2
import pytesseract

image = cv2.imread(filename="temp/test2.png")


def GaussianBlurEffect(grayscale_img):
    gaussian = cv2.GaussianBlur(grayscale_img, (7, 7), 0)
    return gaussian


def threshold(blur_img):
    thresh = cv2.threshold(blur_img, 0, 125, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return thresh


if __name__ == "__main__":
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_img = GaussianBlurEffect(gray_img)
    thresh_img = threshold(blur_img)

    #cv2.imshow(winname="Gray image", mat=gray_img)
    # cv2.imshow(winname="Gaussian image", mat=GaussianBlurEffect(gray_img))
    # cv2.imshow(winname="Thresh image", mat=threshold(GaussianBlurEffect(gray_img)))

    kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 7))
    dilate = cv2.dilate(thresh_img, kernal, iterations=1)

    cv2.imshow("Image test", dilate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
