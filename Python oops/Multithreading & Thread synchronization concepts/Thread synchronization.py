from threading import *

#1
# class Flight:
#     def __init__(self, available_seat):
#         self.available_seat = available_seat
#         self.l = Lock()
#
#     def reserve(self,need_seat):
#         self.l.acquire()
#         print('Available seats', self.available_seat)
#         if self.available_seat >= need_seat:
#             name = current_thread().name
#             print(f'{need_seat} is alloted for {name}')
#             self.available_seat -= need_seat
#         else:
#             print('Sorry! All seats are alloted')
#         self.l.release()
#
# f= Flight(2)
# t1= Thread(target=f.reserve, args=(1,), name='Rahul')
# t2= Thread(target=f.reserve, args=(1,), name='Sonam')
# t3 = Thread(target=f.reserve, args=(1,), name='Raj')
# t1.start()
# t2.start()
# t3.start()


#2 race condition can also happens when blocking = False
# class Flight:
#     def __init__(self, available_seat):
#         self.available_seat = available_seat
#         self.l = Lock()
#
#     def reserve(self,need_seat):
#         self.l.acquire(blocking= False)
#         print('Available seats', self.available_seat)
#         if self.available_seat >= need_seat:
#             name = current_thread().name
#             print(f'{need_seat} is alloted for {name}')
#             self.available_seat -= need_seat
#         else:
#             print('Sorry! All seats are alloted')
#         self.l.release()
#
# f= Flight(2)
# t1= Thread(target=f.reserve, args=(1,), name='Rahul')
# t2= Thread(target=f.reserve, args=(1,), name='Sonam')
# t3 = Thread(target=f.reserve, args=(1,), name='Raj')
# t1.start()
# t2.start()
# t3.start()

#Main Thread can also execute locked resource
# class Flight:
#     def __init__(self, available_seat):
#         self.available_seat = available_seat
#         self.l = Lock()
#
#     def reserve(self,need_seat):
#         self.l.acquire(blocking= True)
#         print('Available seats', self.available_seat)
#         if self.available_seat >= need_seat:
#             name = current_thread().name
#             print(f'{need_seat} is alloted for {name}')
#             self.available_seat -= need_seat
#         else:
#             print('Sorry! All seats are alloted')
#         self.l.release()
#
# f= Flight(2)
# t1= Thread(target=f.reserve, args=(1,), name='Rahul')
# t2= Thread(target=f.reserve, args=(1,), name='Sonam')
# t3 = Thread(target=f.reserve, args=(1,), name='Raj')
# t1.start()
# t2.start()
# t3.start()
# t1.join()          #join will execute one by one by one
# t2.join()
# t3.join()
# print('Main Thread')      #This way Main Thread will join/execute at the last.


#3 RLock
# class Flight:
#     def __init__(self, available_seat):
#         self.available_seat = available_seat
#         self.l = RLock()
#
#     def reserve(self,need_seat):
#         self.l.acquire(blocking= True)
#         self.l.acquire(blocking=True)
#         print('Available seats', self.available_seat)
#         if self.available_seat >= need_seat:
#             name = current_thread().name
#             print(f'{need_seat} is alloted for {name}')
#             self.available_seat -= need_seat
#         else:
#             print('Sorry! All seats are alloted')
#         self.l.release()
#         self.l.release()
#
# f= Flight(2)
# t1= Thread(target=f.reserve, args=(1,), name='Rahul')
# t2= Thread(target=f.reserve, args=(1,), name='Sonam')
# t3 = Thread(target=f.reserve, args=(1,), name='Raj')
# t1.start()
# t2.start()
# t3.start()
# t1.join()          #join will execute one by one by one
# t2.join()
# t3.join()
# print('Main Thread')

#Semaphore
# class Flight:
#     def __init__(self, available_seat):
#         self.available_seat = available_seat
#         self.l = Semaphore(2)   #assigned 2 threads can execute at the same time
#         print(self.l)
#
#     def reserve(self,need_seat):
#         self.l.acquire(blocking= True)
#         print(self.l._value)             #value shows left_count to acquire the lock
#         print('Available seats', self.available_seat)
#         if self.available_seat >= need_seat:
#             name = current_thread().name
#             print(f'{need_seat} is alloted for {name}')
#             self.available_seat -= need_seat
#         else:
#             print('Sorry! All seats are alloted')
#         self.l.release()
#         self.l.release()
#
#
# f= Flight(2)
# t1= Thread(target=f.reserve, args=(1,), name='Rahul')
# t2= Thread(target=f.reserve, args=(1,), name='Sonam')
# t3 = Thread(target=f.reserve, args=(1,), name='Raj')
# t1.start()
# t2.start()
# t3.start()
# t1.join()          #join will execute one by one by one
# t2.join()
# t3.join()
# print('Main Thread')

#BoundedSemaphore
class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat
        self.l = BoundedSemaphore(2)   #assigned 2 threads can execute at the same time
        print(self.l)

    def reserve(self,need_seat):
        self.l.acquire(blocking= True)
        print(self.l._value)             #value shows left_count to acquire the lock
        print('Available seats', self.available_seat)
        if self.available_seat >= need_seat:
            name = current_thread().name
            print(f'{need_seat} is alloted for {name}')
            self.available_seat -= need_seat
        else:
            print('Sorry! All seats are alloted')
        self.l.release()
        


f= Flight(2)
t1= Thread(target=f.reserve, args=(1,), name='Rahul')
t2= Thread(target=f.reserve, args=(1,), name='Sonam')
t3 = Thread(target=f.reserve, args=(1,), name='Raj')
t1.start()
t2.start()
t3.start()
t1.join()          #join will execute one by one by one
t2.join()
t3.join()
print('Main Thread')
