def search(nums: list[int], target: int) -> int:
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1
        
    left, right = 0, len(nums)-1

    while (left < right):
        midpoint = left + (right - left) // 2
        if (nums[midpoint] > nums[right]):
            left = midpoint + 1
        
        else:
            right = midpoint

    start = left
    left = 0
    right = len(nums) - 1

    if (target >= nums[start] and target <= nums[right]):
        left = start
    else:
        right = start - 1

    while(left <= right):
        midpoint = left + (right - left) // 2
        if (nums[midpoint] == target):
            return midpoint
        
        elif nums[midpoint] > target:
            right = midpoint - 1
        
        else:
            left = midpoint + 1
    
    return -1








myArr = [4,5,6,7,0,1,2]
search(myArr, 8)