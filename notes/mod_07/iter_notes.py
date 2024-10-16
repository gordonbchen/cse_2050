# L = [1, 2]
# my_iter = iter(L)

# print(next(my_iter))
# print(next(my_iter))


# class MyIter:
#     def __iter__(self):
#         self.a = 0
#         return self

#     def __next__(self):
#         self.a += 1
#         if self.a < 10:
#             return self.a

#         raise StopIteration()


# obj = MyIter()
# obj_iter = iter(obj)
# print(next(obj_iter))
# print(next(obj_iter))

# for x in obj_iter:
#     print(x)


def my_generator():
    n = 1
    while n <= 10:
        yield n
        n += 2


for i in my_generator():
    print(i)
