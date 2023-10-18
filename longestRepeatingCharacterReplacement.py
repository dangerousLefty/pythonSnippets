def characterReplacement(s: str, k: int) -> int:
        l = 0
        maxLen = 0
        countLetters = {}

        for r in range(len(s)):
            countLetters[s[r]] = countLetters.get(s[r], 0) + 1
            while k < (r - l + 1) - max(countLetters.values()):
                countLetters[s[l]] -= 1
                l += 1
                
            
            maxLen = max(maxLen, (r - l + 1))
        
        return maxLen


a = characterReplacement("AABABBA", 1)