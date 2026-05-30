class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        complement = 0
        for index, value in enumerate(nums):
            complement = target - value
            if complement in dict_nums:
                return [dict_nums[complement], index]
            dict_nums[value] = index
        return None