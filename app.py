from flask import Flask,request
from paddleocr import PaddleOCR
from gevent.pywsgi import WSGIServer
ocr = PaddleOCR(lang='es', show_log=False)
app = Flask(__name__)

@app.route('/test',methods=['POST'])
def test():
    file = request.files['image']
    file.save(file.filename)
    return imageToText(file.filename)

def imageToText(img):
    try:
        result = ocr.ocr(img, cls=True)
        string = []
        for line in result:
            for x in line:
                string.append(x[-1][0])
        return string
    except:
        return ["none"]

if __name__ == '__main__':
    http_server = WSGIServer(('', 9123), app)
    http_server.serve_forever()

