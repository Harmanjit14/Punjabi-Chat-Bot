# Punjabi-Chat-Bot
Chatbot using iNTK libraray. The implementation is straightforward with a Feed Forward Neural net with 2 hidden layers. Customization for your own use case is super easy. Just modify intents.json with possible patterns and responses and re-run the training (see below for more info).
## Requirements
- Python 3.7
- Torch 1.3.1

## Installation and Ussage
- run ``` pip install -r requirements.txt ``` to install all dependencies
- Add conversation examples to ``` intents.json ``` then re-train the model using ``` train.py ```
- Converse with bot using ``` chat.py ``` file.
