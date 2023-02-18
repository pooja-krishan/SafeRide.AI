from vosk import Model, KaldiRecognizer
import pyaudio
from sentimentAnalysis import getAttributes
    
model = Model(model_name = "vosk-model-small-en-us-0.15")

recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    
    
def transcribe():
    while True:
        data = stream.read(4096)
            
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            text = text[14:-3]
            if text != '':
                print(text)
                print(getAttributes(text))
                
if __name__ == "__main__":
    transcribe()