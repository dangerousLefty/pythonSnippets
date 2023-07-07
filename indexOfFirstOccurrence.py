def strStr(haystack: str, needle: str) -> int:
    # counter = 0
    # initialC = 0
    if len(needle) > len(haystack):
        return -1
    for counter in range(len(haystack)):
        if haystack[counter] == needle[0]:
            needleCount = 0
            initialCount = counter
            tempCounter = counter
            while tempCounter < len(haystack) and haystack[tempCounter] == needle[needleCount]:
                needleCount += 1
                tempCounter += 1
                if needleCount == len(needle):
                    return initialCount
    return -1


def anotherOne(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i] == needle[0]:
            # tempCounter = i
            for j in range(len(needle)):
                # flag = True
                if haystack[i+j] != needle[j]:
                    # flag = False
                    break
                # else:
                #    tempCounter += 1
            if j == len(needle) - 1:
                return i

    return -1


print(anotherOne("hello", "ll"))
