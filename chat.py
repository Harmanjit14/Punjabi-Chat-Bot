from nlp_resolver import *
from google.cloud import texttospeech
import time
import speech_recognition as sr
import os
from playsound import playsound
from queries import *


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"key.json"

language = 'pa-IN'
recognize_language = 'en-US'


bot_name = "Hazel"

client = texttospeech.TextToSpeechClient()
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3)

r = sr.Recognizer()
keyword = "hazel"

obj = Credentials()
# log = case_selector(-1, obj)
# if not log:
#     print('ਮਾਫ਼ ਕਰਨਾ ਮੈਂ ਤੁਹਾਨੂੰ ਲੌਗਇਨ ਕਰਨ ਵਿੱਚ ਅਸਮਰੱਥ ਸੀ')
#     exit()

with sr.Microphone() as source:
    print('Adjusting mic')
    r.adjust_for_ambient_noise(source=source, duration=5)
while True:

    with sr.Microphone() as source:
        print("Listening to Hazel")
        audio = r.listen(source, timeout=1, phrase_time_limit=2)
    try:
        text = r.recognize_google(audio, language=recognize_language)
        print(text)
        if text == 'Hazel' or text == 'hazel':

            with sr.Microphone() as source2:
                print("Listening to Query")
                query = r.listen(source2, timeout=3, phrase_time_limit=5)
            try:
                response = r.recognize_google(query, language=language)
                print(f'User Query: {response}')

                speech_response = nlp_resolver(response, obj)
                print(speech_response)
                synthesis_input = texttospeech.SynthesisInput(
                    text=speech_response)

                voice = texttospeech.VoiceSelectionParams(
                    language_code=language, ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
                response_voice = client.synthesize_speech(
                    input=synthesis_input, voice=voice, audio_config=audio_config)

                file = r'response_file.mp3'
                with open(file, "wb") as out:
                    out.write(response_voice.audio_content)

                playsound(file)
                time.sleep(0.5)
                os.remove(file)

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
