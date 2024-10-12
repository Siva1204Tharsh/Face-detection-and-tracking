import cv2
import matplotlib.pyplot as plt

alg="haarcascade_frontalface_default.xml" # store the path of the algorithm
haar_cascade=cv2.CascadeClassifier(alg) # load the algorithm using sintax

cam=cv2.VideoCapture(0)
while True: #loop until q is pressed
    _,img=cam.read() #read frame from camera 
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=haar_cascade.detectMultiScale(grayImg,1.3,4)  #passing algorithm an
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Face Detection",img)
    # plt.imshow(img)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()