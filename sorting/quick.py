"""
Theoretical runtime is O(n^2) for worst case (already sorted/reverse sorted),
but in practice it has a fast aggregate runtime that tends towards O(n log n),
which is the motivation for its name. The worst case rarely happens.

Worst case for partitioning is if pivot is least/greatest val in the
range of left & right bounds. Best case for pivot is the aprox
median in between left & right bounds. For a worst case scenario, the
in place swapping will tend towards O(n). For a best case scenario, the
in place swapping will tend toward O(log n).

bfort partition > random partition > first & last partition
"""

from random import randint


def first_partition(nums, left_bound, right_bound):
    return _partition(nums, left_bound, right_bound)


def last_partition(nums, left_bound, right_bound):
    nums[left_bound], nums[right_bound-1] = nums[right_bound-1], nums[left_bound]
    return _partition(nums, left_bound, right_bound)


def random_partition(nums, left_bound, right_bound):
    random_index = randint(left_bound, right_bound-1)
    nums[random_index], nums[left_bound] = nums[left_bound], nums[random_index]
    return _partition(nums, left_bound, right_bound)


def bfort_partition(nums, left_bound, right_bound, step=5):
    """blum-floyd-pratt-rivest-tarjan partitioning
    Split the array into blocks and find their medians. The block size
    seems to be arbitrary.
    Return the median of the approx medians in O(n) time.

    https://en.wikipedia.org/wiki/Median_of_medians"""

    all_medians = []

    for i in range(0, len(nums), step):
        if len(nums)-i < step:
            all_medians.append(_find_median(nums, i, len(nums)))
        else:
            all_medians.append(_find_median(nums, i, i+step))

    median_index = _find_median(all_medians)
    nums[left_bound], nums[median_index] = nums[median_index], nums[right_bound]
    _partition(nums, left_bound, right_bound)


def _find_median(nums, left_bound, right_bound):
    """O(n)"""
    pass


def _partition(nums, left_bound, right_bound):
    pivot_val = nums[left_bound]
    first_index = left_bound+1

    for i in range(first_index, right_bound):
        # Move items less than pivot into front of range [left_bound...n-1]
        if nums[i] < pivot_val:
            # swap values
            nums[first_index], nums[i] = nums[i], nums[first_index]
            first_index += 1

    # Move pivot item into final position and return its position
    # index within left & right bound that is in quasi sorted order
    nums[first_index-1], nums[left_bound] = nums[left_bound], nums[first_index-1]
    return first_index-1  # index of pivot val


def quick_sort(nums, partition_method, left_bound=0, right_bound=None):
    if right_bound is None:
        right_bound = len(nums)

    if right_bound-left_bound <= 1:
        return

    pivot = partition_method(nums, left_bound, right_bound)

    quick_sort(nums, partition_method, left_bound, pivot)
    quick_sort(nums, partition_method, pivot+1, right_bound)
