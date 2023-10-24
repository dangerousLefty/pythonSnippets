def search(nums: list[int], target: int) -> int:
        if len(nums) == 0:
            if nums[0] == target:
                return 0
            else:
                return -1

        left = 0
        right = len(nums)-1
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        
        #find pivot or smallest element 
        while left < right:
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

            mid = left + (right - left) // 2

        pivot = left
        left = 0
        right = len(nums)-1
        print("apples")

        if target >= nums[pivot] and target <= right:
            left = pivot
        
        else:
            right = pivot - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                right = mid - 1
            
            else:
                left = mid + 1

        return -1


a = search([1,3],3)