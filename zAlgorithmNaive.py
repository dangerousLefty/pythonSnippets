
def buildZarr(text: str, pattern: str) -> list[int]:
    newString = ''.join([pattern, '$', text])
    zArr = [0 for i in range(len(newString))]

    for i in range(1, len(zArr)-1):
        count = 0
        iStart = i
        for j in range(0, len(zArr)-1):
            while i < len(newString) and newString[j] == newString[i]:
                count += 1
                j += 1
                i += 1
            
            break
            
        zArr[iStart] = count
    
    return zArr

def findMatch(text, pattern)-> list[int]:
    
    zArr = buildZarr(text, pattern)
    mergedString = ''.join([pattern, '$', text])
    outputArr = []

    for i in range(0, len(zArr)-1):
        if zArr[i] == len(pattern):
            outputArr.append(i - (len(pattern) + 1))
    
    return outputArr






a = findMatch("xabcabzabc","abc")

print("apples")