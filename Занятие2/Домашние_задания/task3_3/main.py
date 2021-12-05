def funca(fn):
    def wrapper(*args, **kwargs):
        if not isinstance(fn,)





if __name__ == "__main__":
    # Write your solution here
    pass

def func(*args,**kwargs):
    for index,value in enumerate(args):
        print(f"{index}:{value}")
    for key,value in kwargs.items():
        print(f"{key}:{value}")
func(1, 2, 3, kwarg1="kwarg1", kwarg2="kwarg2")
