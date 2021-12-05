def header_footer(fn):  # TODO написать декоратор
    def wrapper(*arqs, **kwargs):
        print("========")
        fn(*arqs, **kwargs)
        print("========")
    return wrapper




@header_footer
def my_func():
    print("Hello World")


if __name__ == "__main__":
    my_func()
