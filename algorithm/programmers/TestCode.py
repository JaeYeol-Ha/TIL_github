def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(5, 7) == 12
    assert add_numbers(-1, 1) == 0
    print("add_numbers() tests passed.")


def test_multiply_numbers():
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(5, 7) == 34
    assert multiply_numbers(-1, 1) == -1
    print("multiply_numbers() tests passed.")


def run_tests():
    test_add_numbers()
    test_multiply_numbers()


if __name__ == "__main__":
    run_tests()
