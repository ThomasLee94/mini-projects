from merge_sort import merge_sort
from quick_sort import quick_sort, random_partition, \
    median_partition, bfort_partition, first_partition, \
    median_random_partition


def test_merge_sort(nums, sorted_nums):
    assert merge_sort(nums) == sorted_nums
    assert merge_sort(nums) == sorted_nums


# =========================================
def test_quick_sort(nums, sorted_nums):
    test_first_parition(nums, sorted_nums)
    test_random_partition(nums, sorted_nums)
    test_median_partition(nums, sorted_nums)
    test_median_random_partition(nums, sorted_nums)
    test_bfort_partition(nums, sorted_nums)


def test_first_parition(nums, sorted_nums):
    assert quick_sort(nums, first_partition) == sorted_nums


def test_random_partition(nums, sorted_nums):
    assert quick_sort(nums, random_partition) == sorted_nums


def test_median_partition(nums, sorted_nums):
    assert quick_sort(nums, median_partition) == sorted_nums


def test_median_random_partition(nums, sorted_nums):
    assert quick_sort(nums, median_random_partition) == sorted_nums


def test_bfort_partition(nums, sorted_nums):
    assert quick_sort(nums, bfort_partition) == sorted_nums
# =========================================


if __name__ == "__main__":
    nums = [9, 4, 3, 5, 1, 2, 8, 6]
    sorted_nums = [1, 2, 3, 4, 5, 6, 8, 9]

    test_merge_sort(nums, sorted_nums)
    test_quick_sort(nums, sorted_nums)
