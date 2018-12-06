#!/bin/python
# --- encoding: utf-8 ---
#
#
#
#
#
import pytesseract

class Reader:
    def __init__(self):
        pass

    @classmethod
    def getMoney(cls, data):
        tesseract_cmd = "/usr/local/Cellar/tesseract/4.0.0"
        try:
            _image = pytesseract.image_to_string(data, config="--psm 9 sfz")
            if _image:
                return _image.replace("_", "")

            return "0.00"
        except Exception as error:
            return "0.00"
