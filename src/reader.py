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
        _path = path.dirname(__file__)
        _path = path.join(_path, "..", "caches", str(uuid.uuid4()) + ".png")
        _money = "0.00"

        with open(_path, "wb") as up:
            up.write(data['body'])



        try:
            _image = pytesseract.image_to_string(_path, config="--psm 9 sfz")
            if _image:
                _money = _image.replace("_", "")
        except Exception as error:
            pass

        remove(_path)
        return _money
