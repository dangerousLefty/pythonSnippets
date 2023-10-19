def paidStaircase(n: int, p: [int]) -> int:
    stepArr = [1 for i in range(n+1)]

    stepArr[0] = 0
    stepArr[1] = p[1]
    for i in range(2, n+1):
        stepArr[i] = min(stepArr[i-1], stepArr[i-2]) + p[i]
    
    return stepArr[n]


def paidStaircaseOptimized(n: int, k: int, p: [int]) -> int:
    kArr = [1 for i in range(k)]
    for i in range(0,len(kArr)):
        kArr[i] = p[i]

    for i in range(len(kArr), n+1):
        minCost = min(kArr)
        kArr[i % k] = minCost + p[i]

    return kArr[n % k]







#a = paidStaircase(3, [0,3,2,4])

a = paidStaircaseOptimized(3,2,[0,3,2,4])
print(a)