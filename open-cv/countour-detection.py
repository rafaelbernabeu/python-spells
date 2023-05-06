import cv2
import cv2_tools

print('Name: {}\nVersion:{}\nHelp:{}'.format(cv2_tools.name,cv2_tools.__version__,cv2_tools.help))

vid_capture = cv2.VideoCapture(1)

while(vid_capture.isOpened()):
    ret, frame = vid_capture.read()
    if ret == True:
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
        edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)

        # ret, thresh = cv2.threshold(edges, 150, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(image=edges, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
        
        image_copy = frame.copy()
        cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
        cv2.imshow('Contours', image_copy)

        k = cv2.waitKey(20)
        # 113 is ASCII code for q key
        if k == 113:
         break
    else:
        break
 

vid_capture.release()
cv2.destroyAllWindows()