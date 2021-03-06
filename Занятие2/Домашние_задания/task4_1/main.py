def pairwase(iterable):
    for i in range(len(iterable) - 1):
        yield iterable[i], iterable[i + 1]


if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]
    def task():
        for pair in pairwase(pts):
            print(pair)

