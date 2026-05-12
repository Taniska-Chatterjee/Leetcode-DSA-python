class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       
        fill_pos = 0
        
        for num in nums:
            if num != 0:
                nums[fill_pos] = num
                fill_pos += 1
        
        while fill_pos < len(nums):
            nums[fill_pos] = 0
            fill_pos += 1