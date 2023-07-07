def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()  # sort the initial array
    ptrA = 0
    myFinalList = []

    while ptrA <= len(nums) - 3:
        ptrB = ptrA + 1
        ptrC = len(nums) - 1
        remainder = nums[ptrA] * -1
        while ptrB != ptrC:
            sum = nums[ptrB] + nums[ptrC]
            if sum == remainder:
                myList = [nums[ptrA], nums[ptrB], nums[ptrC]]
                myFinalList.append(myList)
                # myFinalList.add([nums[ptrA], nums[ptrB], nums[ptrC]])
                ptrB += 1
                while nums[ptrB] == nums[ptrB - 1] and ptrB < len(nums)-1:
                    ptrB += 1
            elif sum > remainder:
                ptrC -= 1
            else:
                ptrB += 1

        num = nums[ptrA]
        while ptrA <= len(nums) - 1 and nums[ptrA] == num:
            ptrA += 1

    return myFinalList


myArr = [-2, 0, 1, 1, 2]
myNewArr = threeSum(myArr)
print(myNewArr)
