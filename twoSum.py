def twoSum(nums: list[int], target: int) -> list[int]:
    myDict = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in myDict:
            myArr = [i, myDict[diff]]
            return myArr
        else:
            myDict[nums[i]] = i

            print(range(6))


nums = [2, 7, 11, 15]
print(twoSum(nums, 9))
