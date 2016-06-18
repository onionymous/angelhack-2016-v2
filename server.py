from flask import Flask, Response, render_template, request, send_from_directory
import base64, json
from api.emotion import EmotionClient

app = Flask(__name__)

@app.route("/")
def index():
    return "Testing, this is the base page!"

@app.route("/get_frame_sentiment", methods=['POST'])
def get_frame_sentiment():
    imgstring = request.json['data'].replace("data:image/jpeg;base64,", "")
    #print(imgstring)

    imgdata = base64.b64decode(imgstring)
    
    filename = "tmp/sentiment_frame.jpg"
    with open(filename, 'wb') as f:
        f.write(imgdata)
    
    _key = "59e8effcb05b4ab5b37dc2e0f3290315"
    ec = EmotionClient(_key)

    ec_request = ec.process_image_from_path(filename)
    
    ec_response = ec_request.get_raw_result()
    # se = ec_request.get_strongest_emotion()

    print(ec_response)

    results = { 'neutral': 0,
                'contempt': 0,
                'surprise': 0,
                'happiness': 0,
                'anger': 0,
                'sadness': 0,
                'disgust': 0,
                'fear': 0 }

    if not ec_response == []:
        results = ec_response[0]['scores']

    return json.dumps(results)
    # return jsonify(score=str(score))

if __name__ == "__main__":
    app.run()