def longestPalindrome(s: str) -> str:
    def longestSubstring(l: int, r: int):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    result = ""
    for i in range(len(s)):
        sub1 = longestSubstring(i,i)

        if len(sub1) > len(result):
            result = sub1
        
        sub2 = longestSubstring(i,i+1)

        if len(sub2) > len(result):
            result = sub2

    return result


a = longestPalindrome("ab")
print(a)