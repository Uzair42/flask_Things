def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"


# Testing with Tuples
def testing_tuple():
    assert sum ((1,2,3)) == 6


if __name__ == "__main__":
    test_sum()
    testing_tuple()
    print("Everything passed")