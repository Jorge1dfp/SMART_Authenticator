import tkinter as tk
import cv2
import pyautogui
import os
import image_learning as IM
import SMART_Authenticator as SA
import user_maker as UM

def yo():
    SA.primary()

def desty():
    print("Hit")
    SA.close

def actual():
    UM.user_maker("user1.png")
    UM.user_maker("user2.png")
    UM.user_maker("user3.png")
    IM.image_learning()
    
window = tk.Tk()

window.title("Smart-Authenticator")
dummy = True
window.geometry("450x500")
window.attributes("-fullscreen", False)
panel = tk.Label(window)

panel.pack(side = "bottom", fill = "both", expand = "yes")
panel.configure(background="white")

button = tk.Button(panel, text="Check Face", fg="green", command=yo)    
button.pack(side=tk.LEFT)

button2 = tk.Button(panel, text="Quit", fg="red", command=desty)
button2.pack(side=tk.LEFT)

button3 = tk.Button(panel, text="CaptureFace", fg="red", command=actual)
button3.pack(side=tk.LEFT)


if __name__ == "__main__":   
   
    def task():
        #print("hello")
        window.after(2000, task)  # reschedule event in 2 seconds
    window.after(2000, task)

    print("Solid")
    # initializing our video feed


    



window.mainloop() 

