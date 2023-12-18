import collections

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
        if len(nums) == 1 and k == 1:
            return nums

        myDeque = collections.deque()
        finalAns = []
    
        for ptr in range(0, len(nums)):
            if len(myDeque) > 0 and ptr - myDeque[0] >= k:
                myDeque.popleft()
            
            #deque in ascending order
            while len(myDeque) > 0 and nums[ptr] > nums[myDeque[-1]]:
                myDeque.pop()
            
            myDeque.append(ptr)

            if ptr >= k - 1:
                finalAns.append(nums[myDeque[0]])

        return finalAns

a = maxSlidingWindow([1,3,1,2,0,5],3)