"""
Given a sorted array nums, remove the duplicates in-place
such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this
by modifying the input array in-place with O(1) extra memory.
"""


def remove_duplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    last = None
    index = -1
    for i, num in enumerate(nums):
        if last != num:
            index += 1
            if i != index:
                nums[index] = num
            last = num

    return index + 1


def main():
    """main function"""
    nums = [1, 1, 2]
    assert remove_duplicates(nums) == 2, remove_duplicates(nums)
    assert nums[:2] == [1, 2]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert remove_duplicates(nums) == 5
    assert nums[:5] == [0, 1, 2, 3, 4]
    nums = []
    assert remove_duplicates(nums) == 0


if __name__ == "__main__":
    main()
