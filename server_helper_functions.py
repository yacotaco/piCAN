# helper functions for server
import cv2
import base64

def generate_stream():
    cap = cv2.VideoCapture(0)
    if cap.isOpened() == True:
        while True: 
            ret, frame = cap.read() 
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            retval, buffer = cv2.imencode('.jpg', image)
            img_str = base64.b64encode(image)
            out = "data:image/jpeg;base64,{0}".format(img_str)
            yield out
