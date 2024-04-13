import math

from typing import List


def encrypt(text: str) -> List[str]:
    grid: List[str] = []

    text = "".join(text.split(" "))

    length = len(text)
    square_root_length = math.sqrt(length)
    rows = math.floor(square_root_length)
    columns = math.ceil(square_root_length)

    for index in range(rows):
        start: int = columns * index
        substring = text[start:start + columns]
        grid.append(substring)

    return grid


if __name__ == "__main__":
    txt: str = "if man was meant to stay on the ground god would have given us roots."
    grid: List[str] = encrypt(txt)
    print(grid)
