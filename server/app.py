from vosk import Model, KaldiRecognizer
import pyaudio
from utils.sentimentAnalysis import getPerspectiveScore, getGPTScore
from utils.webcam import webcamController
import threading
from flask import Flask, jsonify, Response


model = Model(model_name = "vosk-model-small-en-us-0.15")

score_history = [0, 0, 0]   # tracks last 5 responses
response_history = ['', '', '']

recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

                    
webcamcontroller = webcamController()
webcam_thread = threading.Thread(target=webcamcontroller.run)
webcam_thread.start()


app = Flask(__name__)

def runWebServer():
    app.run()

def speechMonitoring():
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            text = text[14:-3]
            if text != '':
                print(text)
                response_history.pop(0)
                response_history.append(text)
                score_history.pop(0)
                score_history.append(getPerspectiveScore(text))
                # score_history.append(getGPTScore(text))
                average_score = sum(score_history)/len(score_history)
                print(average_score)
                if (average_score > 0.5 and webcamcontroller.streaming == False):
                    print("***************\nSTARTING WEBCAM\n***************")
                    webcamcontroller.streaming = True
                elif (average_score < 0.25 and webcamcontroller.streaming == True):
                    print("***************\STOPPING WEBCAM\n***************")
                    webcamcontroller.streaming = False

@app.route('/')
def sendStreamStatus():
    if webcamcontroller.streaming:
        return '<h1>streaming</h1>'
    else:
        return '<h1>not streaming</h1>'

@app.route('/transcript')
def sendTranscript():
    return jsonify({
        response_history[0]: score_history[0],
        response_history[1]: score_history[1],
        response_history[2]: score_history[2]
    })


@app.route("/stream")
def sendWebcam():
    if webcamcontroller.streaming:
        return Response(webcamcontroller.run(), mimetype = "multipart/x-mixed-replace; boundary=frame")
    else:
        return "<h1>No stream data</h1>"
    



if __name__ == '__main__':
    try:
        serverThread = threading.Thread(target=runWebServer).start()
        monitoringThread = threading.Thread(target=speechMonitoring).start()
    except Exception as e:
        print(str(e))

    