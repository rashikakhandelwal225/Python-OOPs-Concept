from threading import Thread

#1
# class MyThread(Thread):
#     pass
#
# t= MyThread()
# print(t.name)

#2
# class MyThread(Thread):
#      def run(self):
#          print('Run Method')
#
# t= MyThread()
# t.start()

#3
class MyThread(Thread):
     def run(self):
         for i in range(5):
            print('Child Thread\n')

t= MyThread()
t.start()
t.join()   #It will first run child thread to finish its task and make the let the main thread wait
            # till child thread execute completely, it just run the threads one by one entirely instaed of executing threads at the same time
for i in range(5):
    print('Main Thread')