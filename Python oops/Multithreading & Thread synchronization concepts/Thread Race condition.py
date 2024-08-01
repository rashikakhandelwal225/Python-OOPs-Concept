#race condition happens when two mutliple threads are in race to execute same task at the same time
from threading import Thread, current_thread

class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat

    def reserve(self,need_seat):
        print('Available seats', self.available_seat)
        if self.available_seat >= need_seat:
            name = current_thread().name
            print(f'{need_seat} is alloted for {name}')
            self.available_seat -= need_seat
        else:
            print('Sorry! All seats are alloted')

f= Flight(1)
t1= Thread(target=f.reserve, args=(1,), name='Rahul')
t2= Thread(target=f.reserve, args=(1,), name='Sonam')
t1.start()
t2.start()

