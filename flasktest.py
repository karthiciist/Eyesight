from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)

CORS(app)



@app.route('/status', methods=['GET'])
def healthz():
    return sendresponse("EYESIGHT running...", 200)



# sending API response back to client
def sendresponse(message, statuscode):
    print("string - " + message)
    message1 = {"status": statuscode, "string": message}
    response = jsonify(message1)
    response.status_code = statuscode
    return response


@app.errorhandler(400)
def bad_request(error=None):
    message = {
        'status': 400,
        'message': 'Bad Request: ' + request.url + '--> Please check your data payload...'
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3000, threaded=True)