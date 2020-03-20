import pytesseract 
from PIL import Image
img=Image.open('xyz.png')
text=pytesseract.image_to_string(img)
print(text)
