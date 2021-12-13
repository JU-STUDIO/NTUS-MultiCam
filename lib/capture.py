from lib.__init__ import cv2
from lib.__init__ import threading

class camThread(threading.Thread):

    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID

    def run(self):
        print ("Starting " + self.previewName)
        camPreview(self.previewName, self.camID)

def camPreview(previewName, camID):
    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(camID)
    cam.set(cv2.CAP_PROP_FPS,30)

    if cam.isOpened():  # 第一個 Frame 是否存在
        rval, frame = cam.read()
    else:
        rval = False

    while rval:
        cv2.imshow(previewName, frame)
        rval, frame = cam.read()

        key = cv2.waitKey(20)
        if key == 27:  # ESC
            break
    cv2.destroyWindow(previewName)






























# -----------------------------------
eye_cascade = cv2.CascadeClassifier('config\haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('config\haarcascade_frontalface_default.xml')

def detect(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.2,
                                          minNeighbors=3,)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray,
                                            scaleFactor=1.2,
                                            minNeighbors=3,
                                            minSize=(40,40),)
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        for (ex,ey,ew,eh) in eyes:
            frame = cv2.rectangle(frame,(x+ex,y+ey),(x+ex+ew,y+ey+eh),(0,255,0),2)