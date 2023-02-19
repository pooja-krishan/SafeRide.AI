from vosk import Model, KaldiRecognizer
import pyaudio
from sentimentAnalysis import getPerspectiveScore, getGPTScore
from webcam import webcamController
import threading
import cv2

model = Model(model_name = "vosk-model-small-en-us-0.15")

response_history = [0, 0, 0, 0, 0]   # tracks last 5 responses

recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

                    
webcamcontroller = webcamController()
webcam = threading.Thread(target=webcamcontroller.run, args=(cap,))
webcam.start()

if __name__ == "__main__":
    while True:
        data = stream.read(4096, exception_on_overflow=False)
            
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            text = text[14:-3]
            if text != '':
                print(text)
                response_history.pop(0)
                response_history.append(getGPTScore(text))
                print(response_history)
                if (sum(response_history)/len(response_history) > 0.5):
                    webcamcontroller.start()
                elif webcam.is_alive():
                    webcamcontroller.stop()