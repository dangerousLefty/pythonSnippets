def topKFrequent(nums: list[int], k: int) -> list[int]:
    outputList = list()
    countList = [list() for i in range(len(nums) + 1)]
    #print(countList)

    numberCounter = dict()
    for i in nums:
        numberCounter[i] = numberCounter.get(i, 0) + 1

    #print(numberCounter)
    for k,v in numberCounter.items():
        countList[v].append(k)
    
    #print(countList)
    for i in range(len(nums)-1, -1, -1):
            if len(countList[i]) == 0:
                continue
            
            else:
                for j in countList[i]:
                    outputList.append(j)
                    k -= 1

                    if k == 0:
                        return outputList

    print(outputList)   
    #return outputList


a = topKFrequent([1], 1)