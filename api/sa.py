import requests
from havenondemand.hodclient import *

URL = "https://api.havenondemand.com/1/api/sync/analyzesentiment/v1"
API_KEY = "bde6e32c-61e9-453f-b876-7a29ab3b478b"

client = HODClient(API_KEY, version="v1")

text = input("Input a string to be analyzed: ")
params = {'text': text}

response = client.get_request(params, HODApps.ANALYZE_SENTIMENT, async=False)
sentiment = response['aggregate']['sentiment']
score = response['aggregate']['score']
print("text: " + text + "\nsentiment: " + sentiment + "\nscore: " + str(score))
