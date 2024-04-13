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


def test_encrypt_with_multiple_spaces():
    txt: str = "   if   man   was   meant    to    stay    on    the ground god    would  have   given us roots.   "
    expected_grid: List[str] = ['ifmanwas', 'meanttos', 'tayonthe', 'groundgo', 'dwouldha', 'vegivenu', 'sroots.']

    grid: List[str] = encrypt(txt)

    assert expected_grid == grid


def test_without_spaces():
    txt: str = "ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots."
    expected_grid: List[str] = ['ifmanwas', 'meanttos', 'tayonthe', 'groundgo', 'dwouldha', 'vegivenu', 'sroots.']

    grid: List[str] = encrypt(txt)

    assert expected_grid == grid

def test_with_equal_floor_and_ceil():
    txt: str = "ifmanwasmeanttostayontheg"
    expected_grid: List[str] = ['ifman', 'wasme', 'antto', 'stayo', 'ntheg']

    grid: List[str] = encrypt(txt)

    assert expected_grid == grid


def run_all_test():
    test_encrypt_with_multiple_spaces()
    test_without_spaces()
    test_with_equal_floor_and_ceil()

if __name__ == "__main__":
    run_all_test()

    txt: str = "if man was meant to stay on the ground god would have given us roots."
    grid: List[str] = encrypt(txt)
    print(grid)
