
from utils import bag_of_words, token
import random
import json
import torch
from model import NeuralNet
from queries import *

# Load NLP Model Files
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('intents.json', 'rb') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Hazel"

def nlp_resolver(text,obj):
    sentence = token(text)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:

            if tag == intent["tag"]:

                response = intent['responses']
                resp = random.choice(response)
                print("NLP Response ", resp)
                if not isinstance(resp, int):
                    return resp
                else:
                    query_response = case_selector(int(response[0]),obj)
                    return query_response
    else:
        return f"ਮੈਨੂੰ ਸਮਝ ਨਹੀਂ ਆਇਆ"
