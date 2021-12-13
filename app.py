import cv2
from lib.__init__ import time
from lib.multithreading import VideoWriterWidget
from lib.interface import show_control_panel

if __name__ == '__main__':

    for cam in range(1,3):
        cam = VideoWriterWidget(f'Camera - {cam}', cam)

    show_control_panel()

    # while True:
    #     time.sleep(5)
