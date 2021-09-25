def show_number(num: any, reference: int):
    match num:
        case float():
            print(f"{num} is a float")
        case str():
            print(f"{num} is a string")
        case x if type(num) is not int:
            print(f"{num} is a type `{type(x).__name__}`")
        case _ if num < reference:
            print(f"{num} is less than {reference}")
        case 10:
            print(f"{num} is the same as {reference}")
        case 11 | 12:
            print(f"{num} is a little bigger than {reference}")
        case _ if num == reference * 2:
            print(f"{num} is twice the size of {reference}")
        case _:
            print(f"{num} is bigger than {reference}")


if __name__ == "__main__":
    num = 10
    for i in range(12):
        res = num + i
        if i == 3:
            res = {"hello": "world"}
        if i == 5:
            res = 3.14
        if i == 6:
            res = "hello, world"
        if i == 7:
            res = 9
        show_number(res, num)
        print()
