# don't need to import List like in 3.9
def get_me_a_list() -> List[int]:
    return [1, 2, 3]


if __name__ == "__main__":
    print(get_me_a_list())

# Results!
"""
[1,2,3] 
"""
