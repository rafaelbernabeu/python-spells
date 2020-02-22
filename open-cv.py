import cv2

camera = cv2.VideoCapture(0);

_, i = camera.read();

cv2.imshow('Janela', i);

cv2.waitKey(0);