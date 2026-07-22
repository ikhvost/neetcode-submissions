from typing import List

def read_integers() -> List[int]:
    nums = input().split(",")
    return [int(num) for num in nums]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
