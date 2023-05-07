import cv2
from tkinter import *
from tkinter import ttk
from tkinter import font

ascii_chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
ascii_chars = ascii_chars[::-1]
vid_capture = cv2.VideoCapture(0)

def ascii_art(*args) -> None:
    ret, frame = vid_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    height, width = gray.shape
    aspect_ratio = width / height
    new_width = int(width / 6)
    new_height = int(new_width / aspect_ratio * 0.55)
    resized_gray = cv2.resize(gray, (new_width, new_height))

    # Resize the grayscale frame to reduce the number of pixels
    # Map the pixel values to ASCII characters
    ascii_art = ''
    for row in resized_gray:
        for pixel in row:
            ascii_art += ascii_chars[int(pixel / 255 * 9)]
        ascii_art += '\n'
    
    t.configure(width=new_width, height=new_height)
    t.delete('1.0', 'end')
    t.insert('end', ascii_art)

def loop():
    ascii_art()
    root.after(int(1000 / 24), loop)
    
root = Tk()
root.title("ASCII Art")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

small_font = font.Font(family='Menlo', size=7, weight='normal', slant='roman', underline=0, overstrike=0)
t = Text(mainframe, width = 10, height = 5, font=small_font, wrap="none")
# ys = ttk.Scrollbar(mainframe, orient = 'vertical', command = t.yview)
# xs = ttk.Scrollbar(mainframe, orient = 'horizontal', command = t.xview)
# t['yscrollcommand'] = ys.set
# t['xscrollcommand'] = xs.set
# t.insert('end', "Lorem ipsum...\n...\n...")
t.grid(column = 0, row = 0, sticky = 'nwes')
# xs.grid(column = 0, row = 1, sticky = 'we')
# ys.grid(column = 1, row = 0, sticky = 'ns')
mainframe.grid_columnconfigure(0, weight = 1)
mainframe.grid_rowconfigure(0, weight = 1)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.bind("q", exit)
root.bind("<Escape>", exit)
root.bind("<Return>", ascii_art)

root.after(10, loop)
root.mainloop()