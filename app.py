from lib.__init__ import time
from lib.interface import main
from lib.multithreading import VideoWriterWidget

if __name__ == '__main__':

    for cam in range(1,3):
        cam = VideoWriterWidget(f'Camera - {cam}', cam)
    
    showControlPanel = main()

    # while True:
    #     time.sleep(5)