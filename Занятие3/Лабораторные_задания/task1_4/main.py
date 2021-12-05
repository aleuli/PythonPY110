INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE) , "w" as f:
        map(str.upper, INPUT_FILE)
        with open(OUTPUT_FILE), "w" as f1:
            map(str.upper, OUTPUT_FILE)# TODO перезаписать содержимое одного файла в другой


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
