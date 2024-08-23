from flask import Flask,request
from paddleocr import PaddleOCR
ocr = PaddleOCR(lang='es', show_log=False)
app = Flask(__name__)

@app.route('/test',methods=['POST'])
def test():
    file = request.files['image']
    file.save(file.filename)


if __name__ == '__main__':
    app.run()
