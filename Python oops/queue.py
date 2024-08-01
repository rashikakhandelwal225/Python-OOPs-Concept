# from collections import deque
#
# queue = deque()
#
# queue.append(1)
# queue.append(2)
# queue.append(3)
#
# print(queue)
#
# print(queue.popleft())
# print(queue.popleft())
# print(queue)

#asynchronous code
# import asyncio
#
# async def my_coroutine():
#     print('Hello')
#     await asyncio.sleep(1)
#     print('World')
#
# async def main():
#     result = await my_coroutine()
#     print(result)
# #asyncio.run(my_coroutine())
# asyncio.run(main())

# import functools
# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print('Hello')
#
# say_hello()
# print(say_hello.__name__)

list1 = [1, 2, 3]

def double(x):
    return x*2

doubled_number = map(double, list1)
print(list(doubled_number))