from threading import Thread
import cv2

class VideoWriterWidget(object):

    def __init__(self, video_file_name, src=0):
        self.frame_name = str(src)
        self.video_file = video_file_name
        self.video_file_name = '..\\video\\' + video_file_name + '.avi'
        self.capture = cv2.VideoCapture(src)

        self.frame_width = int(self.capture.get(3))
        self.frame_height = int(self.capture.get(4))

        self.codec = cv2.VideoWriter_fourcc('M','J','P','G')
        self.output_video = cv2.VideoWriter(self.video_file_name, self.codec, 30, (self.frame_width, self.frame_height))

        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

        self.start_recording()
        print('initialized {}'.format(self.video_file))
        # return 

    def update(self):
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
                print("flag : ", self.saveFrameflag)
                # if self.saveFrameflag == 1:
                    # print("above write line, type", type(self.frame))
                    # self.show_frame()
                    # self.save_frame()
        

    def show_frame(self):
        if self.status:
            cv2.imshow(self.frame_name, self.frame)

        key = cv2.waitKey(1)
        if key == 27: # ESC
            self.capture.release()
            self.output_video.release()
            cv2.destroyAllWindows()
            exit(1)

    def save_frame(self):
        self.output_video.write(self.frame)
        self.saveFrameflag = 1

    def start_recording(self):
        def start_recording_thread():
            while True:
                try:
                    # self.dummy = 1
                    self.show_frame()
                    self.save_frame()
                except AttributeError:
                    pass
        self.recording_thread = Thread(target=start_recording_thread, args=())
        self.recording_thread.daemon = True
        self.recording_thread.start()

# if __name__ == '__main__':

#     for cam in range(1,3):
#         video_writer_widget = VideoWriterWidget(f'Camera {cam}', cam)

#     while True:
#         time.sleep(5)