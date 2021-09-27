from random import randint


def is_sorted(nums, reversed=False):
    for i in range(len(nums)-1):
        if reversed is False:
            if nums[i] > nums[i+1]:
                return False
        else:
            if nums[i] < nums[i+1]:
                return False

    return True


def unsort(nums):
    for i in range(len(nums)):
        left = randint(0, len(nums)-1)
        right = randint(0, len(nums)-1)
        nums[left], nums[right] = nums[right], nums[left]
