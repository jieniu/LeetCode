# -*- coding: utf-8 -*-
"""remove element
Given an array nums and a value val, remove all instances of that value
in-place and return the new length.

Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave
beyond the new length.
"""


def remove_element(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    delete_index = len(nums) - 1
    for i, num in enumerate(nums):
        if num == val and i <= delete_index:
            while delete_index >= i:
                if nums[delete_index] == val:
                    delete_index -= 1
                else:
                    nums[i] = nums[delete_index]
                    nums[delete_index] = num
                    delete_index -= 1
                    break

    return delete_index + 1


def main():
    """entrance function"""
    nums = [3, 2, 2, 3]
    assert remove_element(nums, 3) == 2
    assert nums[:2] == [2, 2], nums

    nums = [2, 2, 2, 2]
    assert remove_element(nums, 2) == 0, remove_element(nums, 2)
    assert nums[:0] == [], nums[:0]

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    assert remove_element(nums, 2) == 5, remove_element(nums, 2)
    assert nums[:5] == [0, 1, 4, 0, 3], nums[:5]


if __name__ == "__main__":
    main()
