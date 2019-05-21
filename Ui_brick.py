import tkinter as tk
import cv2
import numpy as np


window = tk.Tk()


window.title("S.A.R.A.H")

window.geometry("1920x1080")
window.attributes("-fullscreen", False)

def yo():
    cap = cv2.VideoCapture(0)
    ret = True
    face_cascade = cv2.CascadeClassifier(
        r"C:\Users\T3kn1kal\eclipse-workspace\Unit-7\src\SMART_Authenticator\haarcascade_frontalface_default.xml")
    # loop until feed is broken
    while ret:
        window.update()
        # captures frame by frame
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # provides a region of interest i.e. the face and draws a rectangle around it
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_color = frame[y:y + h, x:x + w]
            roi_gray = gray[y:y + h, x:x + w]

        # shows the feedq
        cv2.imshow('', frame)

        # breaks loop when q is pressed and closes all the windows
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":   
    window = tk.Tk() 
    window.title("S.A.R.A.H")
    window.geometry("500x500")
   
    def task():
        #print("hello")
        window.after(2000, task)  # reschedule event in 2 seconds
    window.after(2000, task)

    print("No")
    yo()
    # initializing our video feed



 
window.mainloop() 

