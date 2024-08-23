@echo off
REM Remember to activate virtual enviroment (venv/anaconda) before executing
REM https://github.com/PaddlePaddle/PaddleOCR/discussions/11490
pyinstaller --onefile app.py --hidden-import imghder --hidden-import imgaug --hidden-import pyclipper --collect-data paddle --collect-all lmdb --collect-all paddleocr --collect-all requests