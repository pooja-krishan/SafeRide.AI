import cv2
import threading


lock = threading.Lock()

class webcamController:

    def __init__(self) -> None:
        self.streaming = False
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    def stop(self):
        self.streaming = False
        
    def start(self):
        self.streaming = True

    def run(self):
        while self.streaming:
            try:
                with lock:
                    ret, frame = self.cap.read()
                    (flag, encodedImage) = cv2.imencode(".jpg", frame)  
                    if not flag:
                        continue 
                yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
                exitKey = cv2.waitKey(10) & 0xFF
                if exitKey == 27:
                    break

            except cv2.error as e:
                print(str(e))

        self.cap.release()



    
