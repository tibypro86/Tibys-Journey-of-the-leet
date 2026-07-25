class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<1:
            return s
        start = 0
        maxlen = 1
        for i in range(1,len(s)):
            oddstart = i - maxlen - 1
            evenstart = i - maxlen
            oddsub = s[oddstart:i+1]
            evensub = s[evenstart:i+1]

            if oddstart >= 0 and oddsub == oddsub[::-1]:
                start = oddstart
                maxlen += 2
            elif evenstart >=0 and evensub == evensub[::-1]:
                start = evenstart
                maxlen += 1
        return s[start: maxlen+start]