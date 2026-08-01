class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = [[] for i in range(len(nums) + 1)]

        for v in nums:
            count[v] = 1 + count.get(v, 0)
        
        for me, chioma in count.items():
            arr[chioma].append(me)
        
        list = []
        for m in range(len(arr) - 1, 0, -1):
            for t in arr[m]:
                list.append(t)
                if len(list) == k:
                    return list
