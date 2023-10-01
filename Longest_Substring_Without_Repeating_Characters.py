# First Attempt 477 / 987 testcases passed

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        prevMap = {}
        prevList = {0:1}
        lenght_s = ''
        count = 0
        if len(s) == 0:
            return 0
        for char in s:
            if char not in prevMap:
                prevMap[char] = count;
                lenght_s += char
                count += 1
                if prevList[0] < len(lenght_s):
                    prevList[0] = len(lenght_s)
            else:
                count = 0
                prevMap = {}
                prevMap[char] = count
                lenght_s = char

        return prevList[0]

# Second Attempt w Solution

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        max_length = 0
        left = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length