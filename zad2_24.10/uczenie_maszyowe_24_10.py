# -*- coding: utf-8 -*-
"""uczenie_maszyowe_24.10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10GCetGp1NIvpiP_KJv4pqtQjGBmDmUzi
"""



import pytesseract
import cv2


img = cv2.imread('obraz.png')
extractedInformation = pytesseract.image_to_string(img)
print(extractedInformation)

img = cv2.imread('handwritten_1.jpg')
extractedInformation = pytesseract.image_to_string(img)
print(extractedInformation)

img = cv2.imread('handwritten_2.jpg')
extractedInformation = pytesseract.image_to_string(img)
print(extractedInformation)

img = cv2.imread('text_1.png')
extractedInformation = pytesseract.image_to_string(img)
print(extractedInformation)

img = cv2.imread('color_text.jpg')
extractedInformation = pytesseract.image_to_string(img)
print(extractedInformation)



