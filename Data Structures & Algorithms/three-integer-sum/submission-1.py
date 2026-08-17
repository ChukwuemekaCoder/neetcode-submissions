class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        s_nums = sorted(nums)

        for i, n in enumerate(s_nums):
            if i > 0 and n == s_nums[i - 1]:
                continue
            
            left, right = i + 1, len(s_nums) -  1
            while left < right:
                threeSum = s_nums[i] + s_nums[left] + s_nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([s_nums[i], s_nums[left], s_nums[right]])
                
                    left += 1
                    while s_nums[left] == s_nums[left - 1] and left < right:
                        left += 1
        return res