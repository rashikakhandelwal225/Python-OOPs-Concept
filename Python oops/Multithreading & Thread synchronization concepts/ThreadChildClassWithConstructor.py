from threading import Thread

# class MyThread(Thread):
#     def __init__(self):
#         Thread.__init__(self)     #Call parent class constructor
#         print('Child Class constructor')
#
#     def run(self):
#         pass
#
# t= MyThread()
# t.start()

#2
class MyThread(Thread):
    def __init__(self, a):
        Thread.__init__(self)     #Call parent class constructor
        print('Child Class constructor', a)

    def run(self):
        pass

t= MyThread(10)
t.start()