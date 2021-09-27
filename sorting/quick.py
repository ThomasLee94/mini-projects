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

quick sort with bfort partition (median of medians) will have a worst case of
O(n log n) instead of O(n^2) with the other partitioning methods. The important
"gotcha" for bfort partitioning is that finding the medians of the blocks of 5
will cancel out as constant asymptotically
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


def median_of_three_partition(nums, left_bound, right_bound):
    median_index = _median_of_three(nums, left_bound, (left_bound+right_bound)//2, right_bound-1)
    nums[median_index], nums[left_bound] = nums[left_bound], nums[median_index]
    return _partition(nums, left_bound, right_bound)


def bfort_partition(nums, left_bound, right_bound, step=5):
    """blum-floyd-pratt-rivest-tarjan partitioning

    Split the array into blocks of length 5 and find their medians.
    The block size must be of length 5 to achieve the asymptotic bound of
    O(n).

    For proof, refer to the README

    Return the median of the medians in O(n) time.

    https://en.wikipedia.org/wiki/Median_of_medians"""

    median_indices = []  # [(val, index), ...]

    for i in range(0, right_bound, step):
        if right_bound-i < step:
            print("end")
            median_indices.append(_find_median(nums, i, right_bound))
        else:
            print("before end")
            median_indices.append(_find_median(nums, i, i+step))

    median_index = _median_of_medians(median_indices)
    nums[median_index], nums[left_bound] = nums[left_bound], nums[median_index]
    _partition(nums, left_bound, right_bound)


def _median_of_three(nums, i1, i2, i3):
    if nums[i1] > nums[i2]:
        if nums[i2] > nums[i3]:
            return i2
        else:  # i2 < i1 and i2 < i3
            if nums[i1] > nums[i3]:
                return i3
            else:  # i2 < i1 < i3
                return i1
    else:  # i1 < i2
        if nums[i1] > nums[i3]:
            return i1
        else:  # i1 < i3 and i1 < i2
            if nums[i2] > nums[i3]:
                return i3
            else:  # i1 < i2 < i3
                return i2


def _find_median(nums, left_bound, right_bound):
    """O(n) runtime

    Another way of asking this problem is finding the k-th
    order statistic (https://en.wikipedia.org/wiki/Order_statistic)"""
    # TODO: probably a better way of doing this, do I need to sort?
    temp_arr = nums[left_bound:right_bound]
    temp_dict = {nums[i]: i for i in range(left_bound, right_bound)}

    # quick_sort(temp_arr, random_partition)
    temp_arr.sort()

    # val, index
    median_index = len(temp_arr)//2
    return temp_arr[median_index], temp_dict[temp_arr[median_index]]


def _median_of_medians(arr):
    arr = sorted(arr, key=lambda arr: arr[0])
    return arr[len(arr)//2][1]  # return index of median of medians


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
