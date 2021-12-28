from lib.__init__ import cv2
from lib.__init__ import threading

class VideoWriterWidget(object):
    def __init__(self, video_file_name, src=0):
        
        # 開始儲存控制
        # self.saveFrameflag = saveFrameflag

        # VideoCapture 物件
        self.frame_name = str(src)
        self.video_file = video_file_name
        # self.video_file_name = 'video\\' + video_file_name + '.avi'
        self.capture = cv2.VideoCapture(src)
        self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 30)


        # 定義要儲存的寬和高
        self.frame_width = int(self.capture.get(3))
        self.frame_height = int(self.capture.get(4))

        # 定義檔案編碼與存檔定義
        # self.codec = cv2.VideoWriter_fourcc('M','J','P','G')
        # self.output_video = cv2.VideoWriter(self.video_file_name, self.codec, 30, (self.frame_width, self.frame_height))
        self.output_frame_num = 0

        # 啟動執行緒讀取Frame
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

        # 啟動執行緒
        self.start_recording()
        print('initialized {}'.format(self.video_file))

    def update(self):
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
                cv2.putText(self.frame, str(self.output_frame_num), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

    def show_frame(self):
        if self.status:
            cv2.imshow(self.frame_name, self.frame)

        key = cv2.waitKey(1)
        if key == 27 : # ESC
            self.capture.release()
            # self.output_video.release()
            cv2.destroyAllWindows()
            exit(1)

    def save_frame(self):
        # print(f'video/{self.video_file}/frame_{self.output_frame_num}.png')
        self.output_frame_num += 1
        cv2.imwrite(f'video/{self.video_file}/{self.output_frame_num}.png', self.frame)
        # self.output_video.write(self.frame)

    # 開始儲存執行緒
    def start_recording(self):
        def start_recording_thread():
            while True:
                try:
                    self.show_frame()
                    if self.saveFrameflag:
                        print('saveFrameflag: ', self.saveFrameflag)
                        self.save_frame()
                    else:
                        print('saveFrameflag: ', self.saveFrameflag)
                        # self.output_video.release()
                except AttributeError:
                    pass
        self.recording_thread = threading.Thread(target=start_recording_thread, args=())
        self.recording_thread.daemon = True
        self.recording_thread.start()