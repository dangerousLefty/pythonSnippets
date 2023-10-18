def maxSubArray(nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        currSum = nums[0]
        maxSum = currSum
        for i in nums[1:]:
            if i > currSum + i:
                currSum = i
            
            else: currSum += i

            if currSum > maxSum:
                maxSum = currSum
        
        return maxSum


a = maxSubArray([-2,1,-3,4,-1,2,1,-5,4])