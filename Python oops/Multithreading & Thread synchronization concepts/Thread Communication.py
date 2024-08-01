from threading import Thread, Event, Condition
from time import sleep

#Event
# def light_switch():
#     sleep(3)
#     e.set()
#     print('Green Light ON')
#     sleep(5)
#     print('Red Light ON')
#     e.clear()
#
# def traffic():
#     e.wait()
#     while e.is_set():
#         print('You can go...')
#         sleep(0.5)
#     print('Program done')
#
# e= Event()
# t1= Thread(target=light_switch)
# t2 = Thread(target=traffic)
# t1.start()
# t2.start()

# #2. Condition
# lst = []
#
# def produce():
#     cv.acquire()
#     for i in range(1, 6):
#         lst.append(i)
#         sleep(1)
#         print('Item produced')
#     cv.notify()
#     cv.release()
#
# def consume():
#     cv.acquire()
#     cv.wait(timeout=0)
#     cv.release()
#     print(lst)
#
# cv= Condition()
# t1 = Thread(target=produce)
# t2 = Thread(target=consume)
#
# t1.start()
# t2.start()

#3 Queue

