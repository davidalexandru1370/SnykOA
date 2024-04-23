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
   
    difference_letters = rows * columns
    if difference_letters < length:
        grid.append(text[difference_letters:])

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


def test_with_not_perfect_square_length():
    txt: str = "a" * 24
    expected_grid: List[str] = ["aaaaa", "aaaaa", "aaaaa", "aaaaa", "aaaa"]

    grid: List[str] = encrypt(txt)

    assert expected_grid == grid
    

def run_all_test():
    test_encrypt_with_multiple_spaces()
    test_without_spaces()
    test_with_equal_floor_and_ceil()
    test_with_not_perfect_square_length()

if __name__ == "__main__":
    print("Running all tests...")
    run_all_test()
    print("All tests passed.")

    txt: str = "if man was meant to stay on the ground god would have given us roots."
    grid: List[str] = encrypt(txt)
    for word in grid:
        print(word)

    text2: str = "a" * 24
    grid = encrypt(text2)

    for word in grid:
        print(word)
