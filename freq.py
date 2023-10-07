import telnetlib

def dynamic_freq(counter, tn, freq, slice):

    #hardcoded
    format = "slice t "
    type = "C"

    #dynamic
    content = f"{format}{slice} {freq}"
    message = f"{type}{counter}|{content}"
    print("MESSAGE:", message)

    # Send data
    tn.write(message.encode() + b'\r\n')