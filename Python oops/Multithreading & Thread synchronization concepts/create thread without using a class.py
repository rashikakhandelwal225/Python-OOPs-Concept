from threading import Thread
#1
# def disp():
#     print("Thread running")
#
# t=Thread(target=disp)
# t.start()

#2
# def disp(a):
#     print("Thread running", a)
#
# t=Thread(target=disp, args=(10,) )
# t.start()

#3
# def disp(a, b):
#     print("Thread running", a, b)
#
# t=Thread(target=disp, args=(10,20) )
# t.start()

#4
#if we want to execute a thread multiple times
# def disp(a, b):
#     print("Thread running", a, b)
#
# for i in range(5):
#     t=Thread(target=disp, args=(10,20) )
#     t.start()

#5 Order of running of child and main thread is not controlled by you
#Child Thread is independent of Main Thread. There is no dependency between them.
# def disp():
#     for i in range(5):
#         print("Child Thread ")
#
# t=Thread(target=disp)
# t.start()
#
# for i in range(5):
#     print("Main Thread")

#6 publishing 10 videos by distributing 5 videos to child thread and 5 videos to main thread . This way it was fastly and efficiently
#publish videos at the same time by both child and main thread. Instead of publishing videos 1 by 1 in for loop in range(10) which is done
#by single thread
def disp():
    for i in range(5):
        print("publish video c ")

t=Thread(target=disp)
t.start()

for i in range(5):
    print("publish video m")