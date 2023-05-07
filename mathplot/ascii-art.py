import cv2
import matplotlib.pyplot as plt
import numpy as np

# ASCII characters to use for mapping pixel values
ascii_chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

vid_capture = cv2.VideoCapture(0)
cv2.waitKey(500)

ret, frame = vid_capture.read()
vid_capture.release()

if ret == True:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    height, width = gray.shape
    aspect_ratio = width / height
    new_width = 120
    new_height = int(new_width / aspect_ratio * 0.55)
    resized_gray = cv2.resize(gray, (new_width, new_height))

    # Resize the grayscale frame to reduce the number of pixels
    # Map the pixel values to ASCII characters
    ascii_art = ''
    ascii_art_matrix = np.empty((new_height, new_width, 1), dtype=str)
    for i, row in enumerate(resized_gray):
        for j, pixel in enumerate(row):
            ascii_char = ascii_chars[int(pixel / 255 * 9)]
            ascii_art_matrix[i][j] = ascii_char
            ascii_art += ascii_char
        ascii_art += '\n'

    print(ascii_art)
    # Display the ASCII art using matplotlib
    # (fig, ax) = plt.subplots()
    # ax.text(0, 0, ascii_art, fontfamily='monospace', color='black')
    # plt.show()