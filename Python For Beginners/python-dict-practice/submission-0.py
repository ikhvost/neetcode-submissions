from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    counter = {}
    for char in word:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter

# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
