class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMap = {}
        for i, n in enumerate(nums): # [(0, 5), (1, 4), (2, 3)] (i, n)
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i] 
            prevMap[n] = i # {diff, diff, diff}
        return
