from lib.__init__ import cv2
from lib.multithreading import VideoWriterWidget

import tkinter as tk

class  ControlPanel:

    def __init__(self, parent):
        self.parent = parent
        self.frameNum = 0
        self.create_gui()
 
    def create_gui(self):
        self.start_save_btn = tk.Button(self.parent, text='開始儲存', width=20, command=self.start_save).place(x=10, y=10)
        self.end_save_btn = tk.Button(self.parent, text='結束儲存', width=20, command=self.end_save).place(x=240, y=10)

        self.prev_frame_btn = tk.Button(self.parent, text='<F', width=20, command=self.prev_frame).place(x=10, y=50)
        self.next_frame_btn = tk.Button(self.parent, text='F>', width=20, command=self.next_frame).place(x=240, y=50)

    def start_save(self):
        VideoWriterWidget.saveFrameflag = True

    def end_save(self):
        VideoWriterWidget.saveFrameflag = False

    def show_frame(self,frame_num):
        for camNum in range(1,3):
            framePath = f'video\\Camera - {camNum}\\{frame_num}.png'
            image = cv2.imread(framePath)
            cv2.imshow(f'Cam{camNum}', image)
    
    def next_frame(self):
        self.frameNum += 1
        self.show_frame(self.frameNum)

    def prev_frame(self):
        self.frameNum -= 1
        self.show_frame(self.frameNum)

def main():
    root = tk.Tk()
    root.title("控制面板")
    root.geometry('400x100') # 寬*高
    showControlPanel = ControlPanel(root)
    root.mainloop()