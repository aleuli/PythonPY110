def my_enumerate(iterable, start=1):
    indexes = range(start, len(iterable) + start)
    return zip(indexes, iterable)




if __name__ == "__main__":
    # Write your solution here
    pass

list_ = [1, 2, 3, 4, 5]
func = my_enumerate(list_)
for _ in range(len(list_) + 1):
    print(next(func))