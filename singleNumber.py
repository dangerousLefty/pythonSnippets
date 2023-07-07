def singleNumber(nums: list[int]) -> int:

    xor = 0
    for num in nums:
        xor ^= num

    return xor


myArr = [4, 1, 2, 1, 2]
print(singleNumber(myArr))
