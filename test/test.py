import datetime
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageGrab
import cv2
import numpy as np
import threading

VIDEO_SIZE = (960, 540)

cap = cv2.VideoCapture(0)

date = datetime.datetime.now()
filename='rec_%s%s%s%s%s%s.avi' % (date.year, date.month, date.day,
                                                     date.hour, date.minute, date.second)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
frame_rate = 12

out = cv2.VideoWriter()

# --- screen capture

def recording_screen():
    global recording
    recording = True
    while recording:
        img = ImageGrab.grab()
        frame = np.array(img)
        curpos = root.winfo_pointerx(), root.winfo_pointery()
        cv2.circle(frame, curpos, 10, (0,255,255), 2)
        frame = cv2.resize(frame, VIDEO_SIZE)
        tkimage.paste(Image.fromarray(frame))
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)

def start_recording():
    rec_btn.config(state='disabled')
    stop_btn.config(state='normal')
    if not out.isOpened():
        out.open(filename, fourcc, frame_rate, VIDEO_SIZE)
    threading.Thread(target=recording_screen, daemon=True).start()

def stop_recording():
    global recording
    recording = False
    rec_btn.config(state='normal')
    stop_btn.config(state='disabled')

# --- webcam

webcam = None
WEBCAM_SIZE = (280, 200)

def read_frame(imgbox):
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, WEBCAM_SIZE)
            image = Image.fromarray(frame)
            imgbox.image.paste(image)
        webcam.after(20, read_frame, imgbox)

def stop_webcam(event):
    global webcam
    if webcam:
        webcam.destroy()
        webcam = None

def start_webcam():
    global webcam
    if webcam is None:
        webcam = tk.Toplevel()
        webcam.geometry('{}x{}+5+520'.format(WEBCAM_SIZE[0], WEBCAM_SIZE[1]))
        webcam.overrideredirect(1)
        imgbox = tk.Label(webcam)
        imgbox.pack()
        imgbox.image = ImageTk.PhotoImage(image=Image.new('RGB',WEBCAM_SIZE,(0,0,0)))
        imgbox.config(image=imgbox.image)
        webcam.bind('q', stop_webcam)
        read_frame(imgbox)

# --- main

root = tk.Tk()

tkimage = ImageTk.PhotoImage(Image.new('RGB', VIDEO_SIZE, (0,0,0)))

w, h = VIDEO_SIZE
vbox = tk.Label(root, image=tkimage, width=w, height=h, bg='black')
vbox.pack()

frame = tk.Frame(root)
frame.pack()

rec_btn = ttk.Button(frame, text='start recording', width=20, command=start_recording)
rec_btn.grid(row=0, column=0, padx=10, pady=10)

stop_btn = ttk.Button(frame, text='stop recording', width=20, command=stop_recording, state='disabled')
stop_btn.grid(row=0, column=1, padx=10, pady=10)

cap_btn = ttk.Button(frame, text='start webcam', width=20, command=start_webcam)
cap_btn.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()

out.release()
cap.release()