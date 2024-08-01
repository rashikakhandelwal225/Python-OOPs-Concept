from threading import Thread
from time import sleep
# class MyThread:
#     def disp(self, a, b):
#         print(a, b)
#
# myt= MyThread()   #My class object
# t = Thread(target=myt.disp, args=(10, 20))    #create a thread
# t.start()

#Single Tasking: executing multiple task by a thread one by one
# class MyExam():
#     def solve_question(self):
#         self.q1()           #task1
#         self.q2()           #task2
#         self.q3()           #tasl3
#
#     def q1(self):
#         print("Question 1 solved")
#         sleep(3)
#
#     def q2(self):
#         print("Question 2 solved")
#         sleep(3)
#
#     def q3(self):
#         print("Question 3 solved")
#         sleep(3)
#
# myE = MyExam()
#
# t = Thread(target=myE.solve_question)
# t.start()

#Mutlitasking : When multiple task is executed by multiple threads.
#Two task using two threads
class Hotel():
    def __init__(self, t):   # here t is the task
        self.t = t

    def food(self):
        for i in range(1, 6):
            print(self.t, i)



task1 = Hotel('Take Order from Table')
task2 = Hotel('Serve Order to Table')
t1 = Thread(target=task1.food)    #thread 1 performing task 1 ie, h1
t2 = Thread(target=task2.food)
t1.start()
t2.start()

#This situation when multiple task are executed at the same time and show result in a jumbled manner . This is called Thread race condition
#There are ways to solve race condition in python


