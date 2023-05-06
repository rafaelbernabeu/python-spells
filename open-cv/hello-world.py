import cv2
import cv2_tools

print('Name: {}\nVersion:{}\nHelp:{}'.format(cv2_tools.name,cv2_tools.__version__,cv2_tools.help))

# keystroke=27 is the button `esc`
vid_capture = cv2.VideoCapture(1)

while(vid_capture.isOpened()):
    ret, frame = vid_capture.read()
    if ret == True:
        cv2.imshow('Video', frame)
        k = cv2.waitKey(20)
        # 113 is ASCII code for q key
        if k == 113:
         break
    else:
        break


vid_capture.release()
cv2.destroyAllWindows()