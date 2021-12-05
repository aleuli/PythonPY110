def func(fn):
    def wrapper(*args):
        if not isinstance(*args, int):
            return
        result = fn(*args)
        return result
    return wrapper
@func
def funco(list_):
    list_ = 1,3,4,5,6,"o"

