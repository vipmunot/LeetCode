class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxlen = 0
        mydict = {}
        for i in range(len(s)):
            if s[i] in mydict and start <= mydict[s[i]]:
                start = mydict[s[i]] + 1
            else:
                maxlen = max(maxlen,i-start+1)
            mydict[s[i]] = i
        return maxlen