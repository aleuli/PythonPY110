from itertools import count


def task():
    iterator_numbers = count(1, 1)
    numbers = map(lambda x:x ** 2,filter(lambda x:x % 2 == 0,iterator_numbers)) # TODO заменить на map и filter

    for num in range(10):  # TODO напечатать первые 10 чисел
        print(next(numbers))


if __name__ == "__main__":
    task()


# [i ** 2 for i in iterator_numbers if i % 2 == 0]