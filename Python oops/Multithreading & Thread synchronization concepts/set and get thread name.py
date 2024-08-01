from threading import  Thread , current_thread

#1
# def disp():
#     print("Child Thread Object", current_thread())
#
# t= Thread(target=disp)
# t.start()
#
# print("Main Thread Object", current_thread())

#2 getName of current_thread object
# def disp():
#     print("Default Child Thread Name:", current_thread().getName())
#     current_thread().setName('Doctor Thread')
#     print("New Child Thread Name:", current_thread().getName())
#
# t1= Thread(target=disp)
# t1.start()
# t2= Thread(target=disp)
# t2.start()
# #
# #
# print(" Default Main Thread Name:", current_thread().getName())
# current_thread().setName('GeekyShows Thread')
# print("New Main Thread Name:", current_thread().getName())

#3 we can get and set name using name property also
# def disp():
#     print("Default Child:", current_thread().name)
#     current_thread().name = 'Flying Thread'
#     print("New Child:", current_thread().name)
#
# t= Thread(target=disp)
# t.start()

#4 printing default name using getName executed by Main Thread coz we have not written t.start(), print() is by default run by
#main thread
def disp():
    pass

t=Thread(target=disp)
print(t.getName())
t.setName('Doctor Thread')
print(t.getName())
t.name = 'Flying Thread'
print(t.name)

# t= Thread(target=disp)
# print(current_thread())
t= Thread(target=disp, name='Flying Thread')
print(t.name)
print(current_thread())