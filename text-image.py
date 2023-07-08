# Have Fun 
# Free code 
# Made by Mn0g1as

import pytesseract
from PIL import image

image = image.open('PATH/TO/IMAGE.png')
text=pytesseract.image_to_string(image)
print(text)
