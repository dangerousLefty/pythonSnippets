def lengthOfLongestSubstring(s: str) -> int:
        charSet = set()
        l = 0
        maxLen = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[r])
                l += 1
            charSet.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen

lengthOfLongestSubstring("pwwkew")