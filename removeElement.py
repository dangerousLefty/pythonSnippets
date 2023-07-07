def removeElement(nums: list[int], val: int) -> int:
    ptr1 = 0
    ptr2 = 0
    k = len(nums)

    while ptr2 < len(nums):
        if nums[ptr2] == val:
            ptr2 += 1
            k -= 1
        else:
            temp = nums[ptr1]
            nums[ptr1] = nums[ptr2]
            nums[ptr2] = temp
            ptr1 += 1
            ptr2 += 1

    return k


def removeDuplicates(nums: List[int]) -> int:
    ptr1 = 1
    ptr2 = 1

    if len(nums) == 1:
        return 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            ptr1 += 1  # find the next insert point
        else:
            nums[ptr2] = nums[ptr1]
            ptr2 += 1
            ptr1 += 1

    return ptr2


myList = [3, 2, 2, 3]
removeElement(myList, 3)
