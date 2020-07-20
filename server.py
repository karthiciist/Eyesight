from PIL import Image
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import imutils
import cv2
import requests
import shutil
import json


app = Flask(__name__)

bordered_image_saved_file = 'borderedimages/borderedimage.JPG'
url_input_file = 'urlinputs/urlimage.JPG'
local_save_input_file = 'uploadedimages/fromlocal/uploadedimage.JPG'
url_save_input_file = 'uploadedimages/fromurl/uploadedimage.JPG'
bordered_file = 'borderedimages/borderedimage.JPG'

CORS(app)


@app.route('/healthz', methods=['GET'])
def healthz():
    return sendresponse("Aal is well!!!", 200)


@app.route('/border', methods=['POST'])
def border():
    filemode = request.form['filemode']
    if filemode == 'local':
        try:
            bordersize1 = request.form['bordersize']
            image1 = request.files['image']
            bluevalue = request.form['blue']
            greenvalue = request.form['green']
            redvalue = request.form['red']
            image1.save(local_save_input_file)
            image2 = cv2.imread(local_save_input_file)
            name = addborder(image2, bordersize1, bluevalue, greenvalue, redvalue)

            if name == "true":
                return sendresponse("Border added", 200)
            elif name == "false":
                return sendresponse("failed to add border", 201)
            else:
                return sendresponse("failed to add border", 201)

        except Exception as e:
            return sendresponse("failed to add border", 201)

    elif filemode == 'url':
        try:

            bordersize2 = request.form['bordersize']
            url = request.form['url']
            bluevalue = request.form['blue']
            greenvalue = request.form['green']
            redvalue = request.form['red']
            resp = requests.get(url, stream=True)
            local_file = open(url_save_input_file, 'wb')
            resp.raw.decode_content = True
            shutil.copyfileobj(resp.raw, local_file)
            del resp

            image2 = cv2.imread(url_save_input_file)
            name = addborder(image2, bordersize2, bluevalue, greenvalue, redvalue)

            if name == "true":
                return sendresponse("Border added", 200)
            elif name == "false":
                return sendresponse("failed to add border", 201)
            else:
                return sendresponse("failed to add border", 201)

        except Exception as e:
            print(e)
            return sendresponse("failed to rotate image", 201)
    else:
        message = 'Invalid file mode. Pass either \'url\' or \'local\''
        return make_response(jsonify(message=message, status=201), 201)


def addborder(image, bordersize, bluevalue, greenvalue, redvalue):
    try:
        blue = int(bluevalue)
        green = int(greenvalue)
        red = int(redvalue)
        bordersize = int(bordersize)
        borderedimage = cv2.copyMakeBorder(
            image,
            top=bordersize,
            bottom=bordersize,
            left=bordersize,
            right=bordersize,
            borderType=cv2.BORDER_CONSTANT,
            value=[blue, green, red]
        )
        rgbimg = cv2.cvtColor(borderedimage, cv2.COLOR_BGR2RGB)
        image1 = Image.fromarray(rgbimg)
        image1.save(bordered_file)
        return 'true'
    except Exception as e:
        print (e)
        return 'false'



def sendresponse(message, statuscode):
    message1 = {"status": message}
    response = jsonify(message1)
    response.status_code = statuscode
    return response


@app.errorhandler(400)
def bad_request(error=None):
    message = {
        'status': 400,
        'message': 'Bad Request: ' + request.url + '--> Please check your data payload...',
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3000)
