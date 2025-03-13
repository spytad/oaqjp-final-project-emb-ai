import requests, json


def emotion_detector(text_to_analyse): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    # Fallback
    defaultReturn = {'anger': 'None', 'disgust': 'None', 'fear': 'None', 'joy': 'None', 'sadness': 'None', 'dominant_emotion': 'None'}
    '''
    note - the error handling task is poorly conceived.
    how can one return the same dictionary
    if you don't have the keys from the response
    one way or another one has to hard code
    ''' 
    if response.status_code == 400:
        return defaultReturn
        
    formatted_response = json.loads(response.text)    
    r = {}
    keys = list(formatted_response['emotionPredictions'][0]['emotion'].keys())
    for k in keys:
        r[k] = formatted_response['emotionPredictions'][0]['emotion'][k]
    r.update({'dominant_emotion':max(r, key=r.get)})
    return(r)
