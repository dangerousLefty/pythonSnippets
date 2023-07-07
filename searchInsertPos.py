def searchInsert(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    mid = left + (right - left)//2

    while (left <= right):
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
        mid = left + (right - left)//2

    if target > nums[mid]:
        return mid + 1

    else:
        return mid - 1


myArrs = [1, 3, 5, 6]
print(searchInsert(myArrs, 0))
