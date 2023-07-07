def productExceptSelf(nums: list[int]) -> list[int]:
    if len(nums) == 2:
        return nums[nums[1], nums[0]]

    productArray = list(range(len(nums)))
    leftProd = list(range(len(nums)))
    leftProd[0] = 1
    leftProd[1] = nums[0]
    rightProd = list(range(len(nums)))
    rightProd[len(nums)-1] = 1
    rightProd[len(nums)-2] = nums[len(nums) - 1]
    for i in range(2, len(nums)):
        leftProd[i] = leftProd[i-1] * nums[i-1]
    for j in range(len(nums)-3, -1, -1):
        rightProd[j] = rightProd[j+1] * nums[j+1]

    for k in range(len(nums)):
        productArray[k] = leftProd[k] * rightProd[k]

    return productArray


nums = [-1, 1, 0, -3, 3]
print(productExceptSelf(nums))
