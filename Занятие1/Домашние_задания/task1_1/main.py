# def meaning(list_):
#     for _ in iter(list_):
#         return _
#
#
# def index(list_):
#     for _ in iter(index(list_)):
#         return _


def my_enumerate(iterable, start=0):
    indexes = range(start,len(iterable) + start)
    return zip(indexes, iterable)


if __name__ == "__main__":
    # Write your solution here
    pass
    list1 = [1, 2, 3, 4, 5]
    for index1,value in my_enumerate(list1,start=10):
        print(index1,value)

