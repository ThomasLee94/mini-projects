def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    # divide
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    # merge
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def merge(arr_left, arr_right):
    merged = []

    left, right = 0, 0

    while left < len(arr_left) and right < len(arr_right):
        if arr_left[left] < arr_right[right]:
            merged.append(arr_left[left])
            left += 1
        else:
            merged.append(arr_right[right])
            right += 1

    if left != len(arr_left):
        merged.extend(arr_left[left:])
    if right != len(arr_right):
        merged.extend(arr_right[right:])

    return merged


if __name__ == "__main__":
    assert merge_sort([5, 1, 3, 2, 4]) == [1, 2, 3, 4, 5]
    assert merge_sort([19, 10, 11, 13, 12, 15, 10, 17]) == [10, 10, 11, 12, 13, 15, 17, 19]
