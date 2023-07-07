def maxProduct(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    curMax = curMin = res = nums[0]
    for num in nums[1:]:
        tmp = curMax * num
        curMax = max(curMax * num, curMin * num, num)
        curMin = min(curMin * num, tmp, num)
        res = max(res, curMax)
    return res


myArr = [-4, -3, -2]
j = maxProduct(myArr)
print(j)
