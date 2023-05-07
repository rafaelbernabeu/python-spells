import cv2
import cv2_tools
import matplotlib.pyplot as plt

print('Name: {}\nVersion:{}\nHelp:{}'.format(cv2_tools.name,cv2_tools.__version__,cv2_tools.help))

vid_capture = cv2.VideoCapture(1)
cv2.waitKey(1000)

ret, frame = vid_capture.read()
vid_capture.release()

plt.subplot()

if ret == True:
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    plt.imshow(frame)
    plt.show()
       
