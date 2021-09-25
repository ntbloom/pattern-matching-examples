def make_name(idx: int) -> any:
    names = [
        "John",
        "Jean",
        "Giovanni",
        "Johann",
    ]
    return names[idx]


def say_hello(greeting: str, name: str):
    print(f"{greeting}, {name}!")


if __name__ == "__main__":
    for i in range(4):
        name = make_name(i)
        match name:
            case "John":
                g = "Hello"
            case "Jean":
                g = "Bonjour"
            case "Giovanni":
                g = "Buongiorno"
            case "Johann":
                g = "Guten Tag"
            case _:
                g = "None"
        say_hello(g, name)
