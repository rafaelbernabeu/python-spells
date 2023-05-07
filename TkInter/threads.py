from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Feet to Meters")

def start():
    button.configure(text='Stop', command=stop)
    label['text'] = 'Working...'
    global interrupt; interrupt = False
    root.after(1, step)
    
def stop():
    global interrupt; interrupt = True
    
def step(count=0):
    progresss_bar['value'] = count
    if interrupt:
        result(None)
        return
    root.after(10)  # next step in our operation; don't take too long!
    if count == 100:  # done!
        result(42)
        return
    root.after(1, lambda: step(count+1))
    
def result(answer):
    progresss_bar['value'] = 0
    button.configure(text='Start!', command=start)
    label['text'] = "Answer: " + str(answer) if answer else "No Answer"
    
frame = ttk.Frame(root); frame.grid()
button = ttk.Button(frame, text="Start!", command=start); button.grid(column=1, row=0, padx=5, pady=5)
label = ttk.Label(frame, text="No Answer"); label.grid(column=0, row=0, padx=5, pady=5)
progresss_bar = ttk.Progressbar(frame, orient="horizontal", mode="determinate", maximum=100); 
progresss_bar.grid(column=0, row=1, padx=5, pady=5)

root.mainloop()