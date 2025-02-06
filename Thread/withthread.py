import threading

# import withoutthread
# from threading import *

def Hello():
    for i in range(5):
        print('hello ', i)


def Hii():
    for i in range(5):
        print('hii', i)


t1 = threading.Thread(target=Hello)
t2 = threading.Thread(target=Hii)

t1.start()
t2.start()

print("\nThreads started \n")
