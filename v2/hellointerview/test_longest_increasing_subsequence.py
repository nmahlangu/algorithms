import pytest
from longest_increasing_subsequence import Solution


@pytest.fixture
def solution():
    return Solution()


def test_classic_example(solution):
    assert solution.longest_increasing_subsequence_td([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_already_increasing(solution):
    assert solution.longest_increasing_subsequence_td([1, 2, 3, 4, 5]) == 5


def test_strictly_decreasing(solution):
    assert solution.longest_increasing_subsequence_td([5, 4, 3, 2, 1]) == 1


def test_single_element(solution):
    assert solution.longest_increasing_subsequence_td([42]) == 1


def test_two_elements_increasing(solution):
    assert solution.longest_increasing_subsequence_td([1, 2]) == 2


def test_two_elements_decreasing(solution):
    assert solution.longest_increasing_subsequence_td([2, 1]) == 1


def test_all_equal(solution):
    assert solution.longest_increasing_subsequence_td([7, 7, 7, 7]) == 1


def test_lis_not_at_end(solution):
    # LIS is [2, 3, 7, 101] but the array ends with 1
    assert solution.longest_increasing_subsequence_td([2, 3, 7, 101, 1]) == 4


def test_negative_numbers(solution):
    assert solution.longest_increasing_subsequence_td([-5, -3, -1, 0, 2]) == 5


def test_mixed_positive_negative(solution):
    # LIS: [-2, 0, 3, 6] -> length 4
    assert solution.longest_increasing_subsequence_td([3, -2, 0, 3, 6, 1]) == 4
