def isAnagram(s: str, t: str) -> bool:
    myHashMap = {}
    if len(s) != len(t):
        return False
    
    for i in s:
        if i not in myHashMap:
            myHashMap[i] = 1
        else:
            myHashMap[i] = myHashMap.get(myHashMap[i]) + 1
    
    for i in t:
        if i not in myHashMap:
            return False
        else:
            myHashMap[i] = myHashMap.get(myHashMap[i]) - 1

            if myHashMap[i] == 0:
                myHashMap.pop(i)
    
    return True 

