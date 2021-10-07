class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = {}
        for idx, i in enumerate(nums):
            if target - i in mapping:
                return [idx, mapping[target-i]]
            mapping[i] = idx
