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
