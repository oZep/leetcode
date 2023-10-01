class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        revered = ''
        for unit in s:
            revered += unit[::-1]
            revered += ' '
        revered = revered[:len(revered)-1] # remove the extra space at the end
        return revered

        