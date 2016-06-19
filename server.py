from flask import Flask, Response, render_template, request, send_from_directory
import base64, json
from api.emotion import EmotionClient
from havenondemand.hodclient import *
from time import time

app = Flask(__name__)

@app.route("/")
def index():
    return "Testing, this is the base page!"

# @app.route("/get_frame_sentiment", methods=['POST'])
# def get_frame_sentiment():
#     #init the timer
#     cur = int(time()) % 10
#     while True:
#         nxt = int(time()) % 10
#         if (cur == nxt):
#             helper()
#             cur = nxt

# def helper():
#     imgstring = request.json['data'].replace("data:image/jpeg;base64,", "")
#     #print(imgstring)

#     imgdata = base64.b64decode(imgstring)
    
#     filename = "tmp/sentiment_frame.jpg"
#     with open(filename, 'wb') as f:
#         f.write(imgdata)
    
#     _key = "59e8effcb05b4ab5b37dc2e0f3290315"
#     ec = EmotionClient(_key)

#     ec_request = ec.process_image_from_path(filename)
    
#     ec_response = ec_request.get_raw_result()
#     # se = ec_request.get_strongest_emotion()

#     print(ec_response)

#     results = { 'neutral': 0,
#                 'contempt': 0,
#                 'surprise': 0,
#                 'happiness': 0,
#                 'anger': 0,
#                 'sadness': 0,
#                 'disgust': 0,
#                 'fear': 0 }

#     if not ec_response == []:
#         results = ec_response[0]['scores']

#     return json.dumps(results)
#     # return jsonify(score=str(score))

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

@app.route("/get_audio", methods=['POST'])
def get_audio():
    mp3string = request.json['data']
    # print(mp3string)

    mp3data = base64.b64decode(mp3string)

    filename = "tmp/tmp_audio.mp3"
    with open(filename, 'wb') as f:
        f.write(mp3data)

    URL_SPEECH = "https://api.havenondemand.com/1/api/async/recognizespeech/v1"
    API_KEY = "0513bd79-7197-48ae-b324-b7d78b68a3da"

    client = HODClient(API_KEY, "v1")
    
    params = {'file': filename}
    response_async = client.post_request(params, HODApps.RECOGNIZE_SPEECH, async=True)
    jobID = response_async['jobID']
    print(response_async)
    print('https://api.havenondemand.com/1/job/result/' + jobID)
    response = requests.get( 'https://api.havenondemand.com/1/job/result/' + jobID, params={'apikey' : API_KEY})
    text = response.json()['actions'][0]['result']['document'][0]['content']

    URL_SENTIMENT = "https://api.havenondemand.com/1/api/sync/analyzesentiment/v1"

    params = {'text': text}
    response = client.get_request(params, HODApps.ANALYZE_SENTIMENT, async=False)
    sentiment = response['aggregate']['sentiment']
    score = response['aggregate']['score']

    results = {'sentiment': sentiment, 'score': score}

    return json.dumps(results)

if __name__ == "__main__":
    app.run()

