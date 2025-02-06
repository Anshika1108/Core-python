import threading
import time

def first():
    print("Hii Ram")
    time.sleep(3)
    print("Bye Ram")

def second():
    print("Hii Shyam")
    print("Bye Shyam")

T1 = threading.Thread(target=first)
T2 = threading.Thread(target=second,daemon=True)

T1.start()
T2.start()