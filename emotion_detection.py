import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json = myobj, headers=header)
    if response.status.code == 200:
        formatted_response = json.loads(response.text)
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
    
        anger = emotion_scores.get('anger', 0.0)
        disgust = emotion_scores.get('disgust', 0.0)
        fear = emotion_scores.get('fear', 0.0)
        joy = emotion_scores.get('joy', 0.0)
        sadness = emotion_scores.get('sadness', 0.0)

        emotions_dict = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
        }
        dominant_emotion = max(emotions_dict, key=emotions_dict.get)

        return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
        }
     elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
