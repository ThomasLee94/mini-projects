def is_sorted(nums, reversed=False):
    for i in range(len(nums)-1):
        if reversed is False:
            if nums[i] > nums[i+1]:
                return False
        else:
            if nums[i] < nums[i+1]:
                return False

    return True
