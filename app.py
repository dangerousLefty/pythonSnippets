"""This file is for blah blah blah """

#climbing stairs with k steps
def climbingStairs(k: int, n:int) -> int:
    if n < 2:
        return 1
    stepArr = [1 for i in range(n+1)]
    stepArr[0] = 1
    stepArr[1] = 1

    for i in range(2,n+1):
        combinations = 0
        for j in range(1,k+1):
            if j > i:
                break

            combinations += stepArr[i-j]
        
        stepArr[i] = combinations

    return stepArr[n]

def climbingStairsKstepsOptimized(k: int, n:int) -> int:
    if n < 2:
        return 1
    stepArr = [0 for i in range(k)]
    stepArr[0] = 1
    stepArr[1] = 1

    for i in range(2,n+1):
        comb = 0
        for j in range(1,k+1):
            if i - j < 0:
                continue
            comb += stepArr[(i-j)%k]
        
        stepArr[i%k] = comb
            

    return stepArr[n % k]




#a = climbingStairs(3,5)
a = climbingStairsKstepsOptimized(2,5)
    

    