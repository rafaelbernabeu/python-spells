import cv2
import cv2_tools

print('Name: {}\nVersion:{}\nHelp:{}'.format(cv2_tools.name,cv2_tools.__version__,cv2_tools.help))

# keystroke=27 is the button `esc`
vid_capture = cv2.VideoCapture(1)

while(vid_capture.isOpened()):
    ret, frame = vid_capture.read()
    if ret == True:
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('Video', frame)
        # Convert to graycsale
        # Blur the image for better edge detection
        img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
        
        # Sobel Edge Detection
        sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
        sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
        sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
        # Display Sobel Edge Detection Images
        cv2.imshow('Sobel X', sobelx)
        cv2.imshow('Sobel Y', sobely)
        cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
        
        # Canny Edge Detection
        edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
        # Display Canny Edge Detection Image
        cv2.imshow('Canny Edge Detection', edges)








        k = cv2.waitKey(20)
        # 113 is ASCII code for q key
        if k == 113:
         break
    else:
        break
 

 
vid_capture.release()
cv2.destroyAllWindows()