# def foo(*args, **kwargs):
#     print('args', args)        #tuple :  args (1, 2, 3)
#     print('kwargs', kwargs)    #{key:value}    #  kwargs {'a': 4, 'b': 5}
#
# foo(1, 2, 3, a=4, b=5)

# #2. try and except
# try:
#     x = x/0
# except ZeroDivisionError as e:
#     print('Error', e)
# else:
#     print('No error occurred')
# finally:
#     print('This block is always executed')

# #3 lambda
# add = lambda x : x+10
# subtract= lambda  x, y : x-y
#
# print(add(9))
# print(subtract(7, 6))

#4 #__str__ and __repr:
# class MyClass:
#     def __str__(self):
#         return 'This is my class object'
#
#     def __repr__(self):
#         return 'MyClass()'
#
# obj = MyClass()
# print(str(obj))
# print(repr(obj))

#5 #list comprehension
# list1 = [x**2 for x in range(10)]
#
# print(list1)

#6 generator
# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#     yield 56
#
# for value in my_generator():
#     print(value)

#7 deep copy and shallow copy
# import copy
#
# original = [1,2 , [3, 4]]
# shallow = copy.copy(original)
# deep = copy.deepcopy(original)
#
# original[2][0] = 5
# print('shallow:', shallow)
# print('deep:', deep)

#8 metaclass
# class Meta(type):
#     def __new__(cls, name, bases, dct):
#         dct['custom_attribute'] = 'Hello world!'
#         return super().__new__(cls, name, bases, dct)
#
# class MyClass(metaclass=Meta):
#     pass
#
# print(MyClass.custom_attribute)

#9 monkey_patched_method : It modify class method at run time with monkey_patched_method.
# class MyClass:
#     def original_method(self):
#         return 'Original method'
#
# obj = MyClass()
# print(obj.original_method())
#
# def monkey_patched_method(self):
#     return 'Monkey patched method'
#
# MyClass.original_method = monkey_patched_method
# obj1 = MyClass()
# print(obj1.original_method())
#

#10 __new__ and __init__
# class MyClass:
#     def __new__(cls, *args, **kwargs ):
#         print("Creating instance")
#         return super().__new__(cls)
#
#     def __init__(self, value):
#         print('Initializing instance')
#         self.value = value
#
# obj = MyClass(10)

# #11 __call__ method
# class MyClass:
#     def __call__(self, value):
#         return f"Called with {value}"
#
# obj = MyClass()
# print(obj(10))   #__call__ method allows the instance of the class to be called as a function.
#                 #It can be used to define callable objects.

# class MyClass:
#     def __call__(self, value):
#         return f"Called with {value}"
#
# obj = MyClass()
# print(obj(10))

# #staticmethod and #classmethod
# class MyClass:
#     @staticmethod
#     def static_method():
#         return 'static method'
#
#     @classmethod
#     def class_method(cls):
#         return f"Class method of {cls}"
#
# print(MyClass.static_method())
# print(MyClass.class_method())

# #is and ==
# a = [1, 2, 3]
# b = a
# c = [1, 2,3]
#
# print(a is b)  # is shows whether two references points to the same object.
# print(a is c)
# print(a==c)  # == shows whether two objects have the same value

#39 @property

# class MyClass:
#     def __init__(self, value):
#         self._value = value
#
#     @property
#     def value(self):
#         return self._value
#
#     @value.setter
#     def value(self, new_value):
#         self._value = new_value
#
# obj = MyClass(10)
# # print(obj.value)
#
# obj.value = 20
# print(obj.value)

#abstract base class
# from abc import ABC , abstractmethod
#
# class MyAbstractClass(ABC):
#     @abstractmethod
#     def my_method(self):
#         pass
#
# class MyClass(MyAbstractClass):
#     def my_method(self):
#         return 'Implemented Method'
#
# obj = MyClass()
# print(obj.my_method())

#  #__del__
# class MyClass:
#      def __del__(self):
#          print('Object is being destroyed')
#
# obj = MyClass()
# del obj

