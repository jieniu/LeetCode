class Solution:
    def reverseList(self, nums):
        if nums is None:
            return None

        if len(nums) == 1:
            return nums[0]

        for i in range(int(len(nums) / 2)):
            tmp = nums[i]

            nums[i] = nums[len(nums) - i - 1]
            nums[len(nums) -i - 1] = tmp
        return nums


    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1):
            if i == 0:
                self.reverseList(nums)
                return
            elif nums[i] <= nums[i-1]:
                continue
            else:
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        tmp = nums[i-1]
                        nums[i-1] = nums[j]
                        nums[j] = tmp
                        
                        for k in range(int(len(nums[i:]) / 2)):
                            tmp = nums[i+k]
                            nums[i+k] = nums[len(nums)-k-1]
                            nums[len(nums)-k-1] = tmp
                        return 


if __name__ == "__main__":
    s = Solution()
    nums = [3,2,1]

    s.nextPermutation(nums)
    print(nums)

        
