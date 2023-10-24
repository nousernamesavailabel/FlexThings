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

button54015 = tk.Button(gui, width=20, text="7.3115", command=lambda: dynamic_freq(counter, tn, "7.3115", "A"))
button69815 = tk.Button(gui, width=20, text="10.1965", command=lambda: dynamic_freq(counter, tn, "10.1965", "A"))
button77015 = tk.Button(gui, width=20, text="13.9545", command=lambda: dynamic_freq(counter, tn, "13.9545", "A"))
button102915 = tk.Button(gui, width=20, text="16.0355", command=lambda: dynamic_freq(counter, tn, "16.0355", "A"))
button135685 = tk.Button(gui, width=20, text="18.2055", command=lambda: dynamic_freq(counter, tn, "18.2055", "A"))
button160355 = tk.Button(gui, width=20, text="20.0195", command=lambda: dynamic_freq(counter, tn, "20.0195", "A"))
button203015 = tk.Button(gui, width=20, text="23.0015", command=lambda: dynamic_freq(counter, tn, "23.0015", "A"))
button279115 = tk.Button(gui, width=20, text="24.4015", command=lambda: dynamic_freq(counter, tn, "24.4015", "A"))
button265015 = tk.Button(gui, width=20, text="26.5015", command=lambda: dynamic_freq(counter, tn, "26.5015", "A"))
button278115 = tk.Button(gui, width=20, text="27.8115", command=lambda: dynamic_freq(counter, tn, "27.8115", "A"))

button54015_b = tk.Button(gui, width=20, text="7.3115", command=lambda: dynamic_freq(counter, tn, "7.3115", "1"))
button69815_b = tk.Button(gui, width=20, text="10.1965", command=lambda: dynamic_freq(counter, tn, "10.1965", "1"))
button77015_b = tk.Button(gui, width=20, text="13.9545", command=lambda: dynamic_freq(counter, tn, "13.9545", "1"))
button102915_b = tk.Button(gui, width=20, text="16.0355", command=lambda: dynamic_freq(counter, tn, "16.0355", "1"))
button135685_b = tk.Button(gui, width=20, text="18.2055", command=lambda: dynamic_freq(counter, tn, "18.2055", "1"))
button160355_b = tk.Button(gui, width=20, text="20.0195", command=lambda: dynamic_freq(counter, tn, "20.0195", "1"))
button203015_b = tk.Button(gui, width=20, text="23.0015", command=lambda: dynamic_freq(counter, tn, "23.0015", "1"))
button279115_b = tk.Button(gui, width=20, text="24.4015", command=lambda: dynamic_freq(counter, tn, "24.4015", "1"))
button265015_b = tk.Button(gui, width=20, text="26.5015", command=lambda: dynamic_freq(counter, tn, "26.5015", "1"))
button278115_b = tk.Button(gui, width=20, text="27.8115", command=lambda: dynamic_freq(counter, tn, "27.8115", "1"))

entry = tk.Entry(gui, width=24)
entry_button = tk.Button(gui, width=20, text="SET FREQ", command=lambda: dynamic_freq(counter, tn, get_text(), "A"))

entry_b = tk.Entry(gui, width=24)
entry_button_b = tk.Button(gui, width=20, text="SET FREQ", command=lambda: dynamic_freq(counter, tn, get_text_b(), "1"))

# Use grid to stack widgets in a vertical column on the left
label.grid(row=0, column=0, sticky=tk.W)
label_b.grid(row=0, column=1, sticky=tk.W)
button54015.grid(row=1, column=0, sticky=tk.W)  # Match the width of the entry box
button69815.grid(row=2, column=0, sticky=tk.W)  # Match the width of the entry box
button77015.grid(row=3, column=0, sticky=tk.W)  # Match the width of the entry box
button102915.grid(row=4, column=0, sticky=tk.W)  # Match the width of the entry box
button135685.grid(row=5, column=0, sticky=tk.W)  # Match the width of the entry box
button160355.grid(row=6, column=0, sticky=tk.W)  # Match the width of the entry box
button203015.grid(row=7, column=0, sticky=tk.W)  # Match the width of the entry box
button279115.grid(row=8, column=0, sticky=tk.W)  # Match the width of the entry box

button54015_b.grid(row=1, column=1, sticky=tk.W)  # Match the width of the entry box
button69815_b.grid(row=2, column=1, sticky=tk.W)  # Match the width of the entry box
button77015_b.grid(row=3, column=1, sticky=tk.W)  # Match the width of the entry box
button102915_b.grid(row=4, column=1, sticky=tk.W)  # Match the width of the entry box
button135685_b.grid(row=5, column=1, sticky=tk.W)  # Match the width of the entry box
button160355_b.grid(row=6, column=1, sticky=tk.W)  # Match the width of the entry box
button203015_b.grid(row=7, column=1, sticky=tk.W)  # Match the width of the entry box
button279115_b.grid(row=8, column=1, sticky=tk.W)  # Match the width of the entry box
entry.grid(row=9, column=0, sticky=tk.W)
entry_b.grid(row=9, column=1, sticky=tk.W)
entry_button.grid(row=10, column=0, sticky=tk.W)  # Match the width of the entry box
entry_button_b.grid(row=10, column=1, sticky=tk.W)  # Match the width of the entry box

# Make the window always on top
gui.wm_attributes("-topmost", 1)

gui.mainloop()
tn.close()
