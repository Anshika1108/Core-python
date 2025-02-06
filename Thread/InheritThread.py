import threading

class Hii(threading.Thread):
    def run(self):
        for i in range(11):
            print("Hii",i)

t1 = Hii()
t1.start()