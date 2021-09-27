def show_number(val: any, reference: int):
    match val:
        case float():
            print(f"{val} is a float")
        case str():
            print(f"`{val}` is a string")
        case x if type(val) is not int:
            print(f"{val} is a type `{type(x).__name__}`")
        case _ if val < 0:
            print(f"{val} is negative")
        case _ if val < reference:
            print(f"{val} is less than {reference}")
        case 10:
            print(f"{val} is the same as {reference}")
        case 11 | 12 | 13:
            print(f"{val} is a little bigger than {reference}")
        case _ if val == reference * 2:
            print(f"{val} is twice the size of {reference}")
        case _:
            print(f"{val} is bigger than {reference}")


if __name__ == "__main__":
    num = 10
    for i in range(12):
        res = num + i
        show_number(res, num)
    for others in [-9, -10, 5, {"hello": "world"},3.14, "hello world"]:
        show_number(others,num)

# Results!
"""
10 is the same as 10
11 is a little bigger than 10
12 is a little bigger than 10
13 is a little bigger than 10
14 is bigger than 10
15 is bigger than 10
16 is bigger than 10
17 is bigger than 10
18 is bigger than 10
19 is bigger than 10
20 is twice the size of 10
21 is bigger than 10
-9 is negative
-10 is negative
5 is less than 10
{'hello': 'world'} is a type `dict`
3.14 is a float
`hello world` is a string
"""
