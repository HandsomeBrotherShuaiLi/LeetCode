class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3 or (len(nums) == 3 and sum(nums)):
            return []
        sorted_nums = sorted(nums)
        if sorted_nums[0] > 0 or sorted_nums[-1] < 0:
            return []
        target = 0
        mapping = {}
        for i in range(len(sorted_nums)-1):
            for j in range(i+1, len(sorted_nums)):
                current_sum = sorted_nums[i] + sorted_nums[j]
                if target - current_sum in mapping:
