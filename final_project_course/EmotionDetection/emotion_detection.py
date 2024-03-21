import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    
    if response.status_code == 400:
        return { 'dominant_emotion': None, 'sadness': None, 'joy': None, 'fear': None, 'disgust': None, 'anger': None }
    
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion']= dominant_emotion
    return emotions
