def make_name(idx: int) -> any:
    return names[idx]


def hi_john(version: str):
    match version:
        case "John":
            g = "Hello"
        case "Jean":
            g = "Bonjour"
        case "Giovanni":
            g = "Buongiorno"
        case "Johann":
            g = "Guten Tag"
        case _:
            print(f"{version} is not a version of John")
            return
    print(f"{g} {version}")


if __name__ == "__main__":
    names = [
        "John",
        "Jean",
        "Juan",
        "Giovanni",
        "Johann",
        "Michael"
    ]
    for name in names:
        hi_john(name)

# Results!
"""
Hello John
Bonjour Jean
Hola, Juan
Buongiorno Giovanni
Guten Tag Johann
Michael is not a version of John
"""