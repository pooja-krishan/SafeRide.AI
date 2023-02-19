import cv2
import threading

class webcamController:

    def __init__(self) -> None:
        self.streaming = False

    def stop(self):
        self.streaming = False
        cv2.destroyAllWindows()
        
    def start(self):
        self.streaming = True

    def run(self, cap):
        while True:
            while self.streaming:
                try:
                    
                    ret, frame = cap.read()

                    cv2.imshow("Dashcam Footage", frame)

                    exitKey = cv2.waitKey(10) & 0xFF
                    if exitKey == 27:
                        break

                except cv2.error as e:
                    print(str(e))



    
