def longestCommonPrefix(strs: list[str]) -> str:
    if len(strs) == 1:
        return strs[0]
    elif strs[0] == "":
        return ""

    prefixIndex = 1
    commonPrefix = ""
    tempPrefix = strs[0][0:prefixIndex]
    while len(tempPrefix) <= len(strs[0]):
        tempPrefix = strs[0][0:prefixIndex]
        for i in range(1, len(strs)):
            if strs[i][0:prefixIndex] == tempPrefix:
                continue
            else:
                return commonPrefix
        commonPrefix += strs[0][prefixIndex-1]
        prefixIndex += 1
        if len(tempPrefix) == len(strs[0]):
            break
    return commonPrefix


def commonPrefix(strs: list[str]) -> str:
    res = ""

    for char in range(len(strs[0])):  # we want to end the loop early
        for word in strs:
            if word[char] != strs[0][char]:
                return res
        res += strs[0][char]
    return res


myList = ["flower", "flow", "flight"]
j = commonPrefix(myList)
print(j)
