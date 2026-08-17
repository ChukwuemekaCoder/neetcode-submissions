class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = []
        left, right = 0, len(heights) - 1

        while left < right: 
            h = min(heights[left], heights[right])
            w = (right) - left
            Area = h * w
            res.append(Area)

            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                left += 1

        return max(res)