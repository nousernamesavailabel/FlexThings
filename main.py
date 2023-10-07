import tkinter as tk
import telnetlib
from freq import *

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

label_b =tk.Label(gui, text="Press to set freq on slice B")

button14100 = tk.Button(gui, width=20, text="14.100", command=lambda: dynamic_freq(counter, tn, "14.100", "A"))
button14074 = tk.Button(gui, width=20, text="14.074", command=lambda: dynamic_freq(counter, tn, "14.074", "A"))

button14100_b = tk.Button(gui, width=20, text="14.100", command=lambda: dynamic_freq(counter, tn, "14.100", "1"))
button14074_b = tk.Button(gui, width=20, text="14.074", command=lambda: dynamic_freq(counter, tn, "14.074", "1"))

entry = tk.Entry(gui, width=24)
entry_button = tk.Button(gui, width=20, text="SET FREQ", command=lambda: dynamic_freq(counter, tn, get_text(), "A"))

entry_b = tk.Entry(gui, width=24)
entry_button_b = tk.Button(gui, width=20, text="SET FREQ", command=lambda: dynamic_freq(counter, tn, get_text_b(), "1"))

# Use grid to stack widgets in a vertical column on the left
label.grid(row=0, column=0, sticky=tk.W)
label_b.grid(row=0, column=1, sticky=tk.W)
button14100.grid(row=1, column=0, sticky=tk.W)  # Match the width of the entry box
button14074.grid(row=2, column=0, sticky=tk.W)  # Match the width of the entry box
button14100_b.grid(row=1, column=1, sticky=tk.W)  # Match the width of the entry box
button14074_b.grid(row=2, column=1, sticky=tk.W)  # Match the width of the entry box
entry.grid(row=3, column=0, sticky=tk.W)
entry_b.grid(row=3, column=1, sticky=tk.W)
entry_button.grid(row=4, column=0, sticky=tk.W)  # Match the width of the entry box
entry_button_b.grid(row=4, column=1, sticky=tk.W)  # Match the width of the entry box

# Make the window always on top
gui.wm_attributes("-topmost", 1)

gui.mainloop()
tn.close()
