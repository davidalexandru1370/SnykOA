THIN_SPACE = "\u2009"


def compute_staircase(steps: int) -> str:
    if steps <= 0:
        return ""

    element: str = "#"

    staircase: str = ""
    number_of_elements = 1

    while steps > 0:
        spaces = ""
        number_of_spaces = steps - 1
        if number_of_spaces > 0:
            spaces = THIN_SPACE * number_of_spaces

        staircase += spaces + (element * number_of_elements) + ("\n" if steps > 1 else "")
        steps -= 1
        number_of_elements += 1

    return staircase


def test_compute_staircase_valid_number():
    expected_result_with_1 = "#"

    staircase = compute_staircase(1)

    assert staircase == expected_result_with_1

    expected_result_with_2 = THIN_SPACE * 1 + "#" + "\n" \
                             + "##"

    staircase = compute_staircase(2)

    assert staircase == expected_result_with_2

    expected_result_with_4 = THIN_SPACE * 3 + "#" + "\n" \
                             + THIN_SPACE * 2 + "##" + "\n" \
                             + THIN_SPACE * 1 + "###" + "\n" \
                             + "####"

    staircase = compute_staircase(4)

    assert expected_result_with_4 == staircase

    expected_result_with_5 = THIN_SPACE * 4 + "#" + "\n" \
                             + THIN_SPACE * 3 + "##" + "\n" \
                             + THIN_SPACE * 2 + "###" + "\n" \
                             + THIN_SPACE * 1 + "####" + "\n" \
                             + "#####"

    staircase = compute_staircase(5)

    assert expected_result_with_5 == staircase


def test_compute_staircase_negative_number():
    staircase: str = compute_staircase(-1)
    assert staircase == ""

    staircase = compute_staircase(-2)

    assert staircase == ""

    staircase = compute_staircase(0)

    assert staircase == ""


def run_all_tests():
    test_compute_staircase_valid_number()
    test_compute_staircase_negative_number()


if __name__ == "__main__":
    run_all_tests()

    n: int = 4
    staircase: str = compute_staircase(n)
    print(staircase)
