#!/bin/python
# --- encoding: utf-8 ---
#
#
#
#
#
import pytesseract
import uuid
from os import path, remove

class Reader:
    def __init__(self):
        pass

    @classmethod
    def getMoney(cls, data):
        tesseract_cmd = "/usr/local/Cellar/tesseract/4.0.0"
        # tesseract_cmd = "/usr"
        _path = path.dirname(__file__)
        _path = path.join(_path, "..", "caches", str(uuid.uuid4()) + ".png")
        _money = "0.00"

        try:
            with open(_path, "wb") as up:
                up.write(data['body'])
        except Exception as error:
            print str(error)

        try:
            _image = pytesseract.image_to_string(_path, config="-psm 9 sfz")
            if _image:
                _money = _image.replace("_", "")
        except Exception as error:
            print str(error)

        remove(_path)
        return _money
