
#Problem:
#   Paid Staircase II
#
#   You are climbing a staircase. It takes n steps to reach the top and you have to
#   pay p[i] to step on the i-th stair. Each time you can climb 1 or 2 steps.
#   Return the cheapest path to the top of the staircase


def paidStaircase(n: int, p: [int]) -> [int]:

    costArr = [tuple() for i in range(n+1)]
    costArr[0] = (0,0)
    costArr[1] = (p[1],0)

    for i in range(2,n+1):
        #find cheaper prior step
        tempTuple = tuple()
        if costArr[i-2][0] < costArr[i-1][0]:
            tempTuple = (costArr[i-2][0] + p[i],i-2)
        
        else:
            tempTuple = (costArr[i-1][0] + p[i], i-1)

        costArr[i] = tempTuple

    #construct the path
    i = len(costArr) - 1
    cheapestPath = []
    cheapestPath.append(i)
    i = costArr[i][1]

    while i != 0:
        cheapestPath.append(i)
        i = costArr[i][1]

    cheapestPath.append(0)
    cheapestPath.reverse()

    return cheapestPath



a = paidStaircase(8, [0,3,2,4,6,1,1,5,3])
print(a)


