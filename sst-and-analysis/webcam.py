import cv2


class webcamController:

    def __init__(self) -> None:
        self.streaming = True

    def stop(self, cap):
        cap.release()
        cv2.destroyAllWindows()
        quit()

    def start(self, cap):
        while self.streaming:
            try:
                while True:
                    ret, frame = cap.read()
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                    cv2.imshow("Dashcam Footage", frame)

                    exitKey = cv2.waitKey(10) & 0xFF
                    if exitKey == 27:
                        break

                self.stop(cap)

            except cv2.error as e:
                print(str(e))




    
