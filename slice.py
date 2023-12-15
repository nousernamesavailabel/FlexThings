def slice(counter, tn, freq, slice, mode ):

    type = "C" #message type set
    content = f"slice t {slice} {freq}"
    message = f"{type}{counter}|{content}"
    print("MESSAGE:", message)

    tn.write(message.encode() + b'\r\n')
    counter=counter+1

    tune = f"{type}{counter}| atu start"
    print(tune)
    tn.write(tune.encode() + b'\r\n')
    counter=counter+1

    type = "C"
    modechange = f"{type}{counter}| slice s {slice} mode={mode}"
    print(modechange)
    tn.write(modechange.encode() + b'\r\n')

def set_mode(counter, tn, slice, mode):
    modechange = f"C{counter}| slice s {slice} mode={mode}"
    print(modechange)
    tn.write(modechange.encode() + b'\r\n')
    counter=counter+1

def tune(counter, tn, slice):
    tune = f"C{counter}| atu start"
    print(tune)
    tn.write(tune.encode() +b'\r\n')
    counter = counter + 1