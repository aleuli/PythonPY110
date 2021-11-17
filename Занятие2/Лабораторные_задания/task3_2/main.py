def min_len_check(fn):
    def wrapper(arq):
        if len(arq) < 10:
            raise ValueError# TODO записать обертку для исходной функции
        result = fn(arq)
        return result
    return wrapper


@min_len_check# TODO задекорировать функцию
def some_func(str_arg: str):
    print(str_arg)


if __name__ == "__main__":
    some_func("Hello, World!!!")  # всё хорошо

    some_func("Short str")  # ValueError("Строка слишком короткая")
