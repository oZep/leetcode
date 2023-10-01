class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n % 2 # 1101 % 2 = 1
            n = n >> 1 # bit shift to the right by 1
        return count