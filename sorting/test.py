from util import is_sorted, unsort
from merge import merge_sort
from quick import median_of_three_partition, quick_sort, random_partition, \
    bfort_partition, first_partition, last_partition


def test_is_sorted():
    sorted_nums_ascending = [1, 2, 3, 4]
    unsorted_nums_ascending = [4, 1, 2, 3]

    sorted_nums_descending = [5, 4, 2, 1]
    unsorted_nums_descending = [5, 4, 1, 3]

    assert is_sorted(sorted_nums_ascending) is True
    assert is_sorted(unsorted_nums_ascending) is False
    assert is_sorted(sorted_nums_descending, True) is True
    assert is_sorted(unsorted_nums_descending, True) is False


def test_unsorted(nums):
    unsort(nums)
    assert is_sorted(nums) is False


def test_merge_sort(nums):
    unsort(nums)
    merged_nums = merge_sort(nums)
    assert is_sorted(merged_nums) is True


# quick sort start =========================================
def test_quick_sort(nums):
    test_first_parition(nums)
    test_last_parition(nums)
    test_random_partition(nums)
    test_median_of_three_partition(nums)
    test_bfort_partition()


def test_first_parition(nums):
    unsort(nums)
    quick_sort(nums, first_partition)
    assert is_sorted(nums) is True


def test_last_parition(nums):
    unsort(nums)
    quick_sort(nums, last_partition)
    assert is_sorted(nums) is True


def test_random_partition(nums):
    unsort(nums)
    quick_sort(nums, random_partition)
    assert is_sorted(nums) is True


def test_median_of_three_partition(nums):
    unsort(nums)
    quick_sort(nums, median_of_three_partition)
    assert is_sorted(nums) is True


def test_bfort_partition():
    nums = [20, 5, 6, 1, 19, 17, 8, 4, 11, 12, 9, 2, 13]
    quick_sort(nums, bfort_partition)
    assert is_sorted(nums) is True
# quick sort end ===========================================


if __name__ == "__main__":
    nums = [9, 4, 3, 5, 1, 2, 8, 6]
    test_is_sorted()
    test_merge_sort(nums)
    test_quick_sort(nums)
