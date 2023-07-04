from PIL import Image#光學辨識外掛(要先安裝:pip install Pillow)
import pytesseract#光學辨識外掛(要先安裝:pip install pytesseract)

def _main():
    try:
        
        pytesseract.pytesseract.tesseract_cmd ="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        #樣先載入次執行檔tesseract.exe
        img = Image.open("C:\\Users\\USER\\Desktop\\validateCodeService.do2.jpg")
        #img = Image.open("C:\\Users\\USER\\Desktop\\中文辨識.jpg")
        #img = Image.open("C:\\Users\\USER\\Desktop\\中英文辨識.png")
        img.show()
        print(pytesseract.image_to_string(img,lang="eng"))
        #print(pytesseract.image_to_string(img,lang="chi_tra+eng"))
        #print(pytesseract.image_to_string(img,lang="chi_tra"))
        #以字串的形式偵測，語言為英文
    except:
        print("再試一次吧")

_main()