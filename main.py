import tkinter as tk
import telnetlib
from freq import *
from slice import *

host = "10.0.0.111"
port = 4992
counter = 6

tn = telnetlib.Telnet(host, port)

def get_text():
    user_input = entry.get()
    print("TEXT:", user_input)
    return user_input

def get_text_b():
    user_input_b = entry_b.get()
    print("TEXT_B:", user_input_b)
    return user_input_b

gui = tk.Tk()
gui.title("FLEX")

label = tk.Label(gui, text="Press to set freq on slice A")

label_b =tk.Label(gui, text="Press to set freq on slice A")

button7074 = tk.Button(gui, width=20, text="7.074", command=lambda: dynamic_freq(counter, tn, "7.074", "A"))
button18100 = tk.Button(gui, width=20, text="18.100", command=lambda: dynamic_freq(counter, tn, "18.100", "A"))

button21074 = tk.Button(gui, width=20, text="21.074", command=lambda: dynamic_freq(counter, tn, "21.074", "A"))
button28074 = tk.Button(gui, width=20, text="28.074", command=lambda: dynamic_freq(counter, tn, "28.074", "A"))


button20mFT8 = tk.Button(gui, width=20, text="20M FT8", command=lambda: slice(counter, tn, "14.074", "A", "digu"))
button20mSSB = tk.Button(gui, width=20, text="20M SSB", command=lambda: slice(counter, tn, "14.225", "A", "usb"))

buttonUSB = tk.Button(gui, width=20, text="USB", command = lambda: set_mode(counter, tn, "A", "USB") )
buttonDIGU = tk.Button(gui, width=20, text="DIGU", command = lambda: set_mode(counter, tn, "A", "DIGU"))

buttonTUNE = tk.Button(gui, width=40, text="Tune", command = lambda: tune(counter, tn, slice))

entry = tk.Entry(gui, width=20)
entry_button = tk.Button(gui, width=20, text="SET FREQ", command=lambda: dynamic_freq(counter, tn, get_text(), "A"))

entry_b = tk.Entry(gui, width=20)
entry_button_b = tk.Button(gui, width=20, text="SET FREQ", command=lambda: dynamic_freq(counter, tn, get_text_b(), "A"))

# Use grid to stack widgets in a vertical column on the left
label.grid(row=0, column=0, sticky=tk.W)
label_b.grid(row=0, column=1, sticky=tk.W)
button7074.grid(row=1, column=0, sticky=tk.W)  # Match the width of the entry box
button18100.grid(row=1, column=1, sticky=tk.W)  # Match the width of the entry box
button21074.grid(row=2, column=0, sticky=tk.W)  # Match the width of the entry box
button28074.grid(row=2, column=1, sticky=tk.W)  # Match the width of the entry box
entry.grid(row=3, column=0, sticky=tk.W)
entry_b.grid(row=3, column=1, sticky=tk.W)
entry_button.grid(row=4, column=0, sticky=tk.W)  # Match the width of the entry box
entry_button_b.grid(row=4, column=1, sticky=tk.W)  # Match the width of the entry box
button20mSSB.grid(row=5, column=1, sticky=tk.W)
buttonUSB.grid(row=6, column = 1, sticky=tk.W)
button20mFT8.grid(row=5, column=0, sticky=tk.W)
buttonDIGU.grid(row=6, column=0, sticky=tk.W)
buttonTUNE.grid(row=9, column=0, columnspan=2)
# Make the window always on top
gui.wm_attributes("-topmost", 1)

gui.mainloop()
tn.close()
