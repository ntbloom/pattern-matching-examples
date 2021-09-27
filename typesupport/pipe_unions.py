# the old way
"""
from typing import Optional
def get_square_if_odd(num: int) -> Optional[int]:
    ...
"""

# or using Unions...
"""
from typing import Union
def get_square_if_odd(num: int) -> Union[int,None]:
    ...
"""


def get_square_if_odd(num: int) -> int | None:
    if num % 2 == 0:
        return None
    else:
        return num ** 2


if __name__ == '__main__':
    for i in range(10):
        print(get_square_if_odd(i))

# Results!
"""
None
1
None
9
None
25
None
49
None
81
"""
