def task(numbers: list) -> int:
    return sum(map(lambda x: x ** 3, filter(lambda x: x < 0, numbers)))


if __name__ == "__main__":
    list_numbers = [-2, -1, 0, 1, -3, 2, -3]
    print(task(list_numbers))
