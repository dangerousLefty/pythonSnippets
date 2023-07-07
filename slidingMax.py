import collections


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:

    myDeque = collections.deque()
    leftPointer = rightPointer = 0
    output = []

    while rightPointer < len(nums):
        while len(myDeque) > 0 and nums[myDeque[-1]] < nums[rightPointer]:
            myDeque.pop()
        myDeque.append(rightPointer)

        # remove left val from window
        if leftPointer > myDeque[0]:
            myDeque.popleft()

        if (rightPointer-leftPointer) == k-1:
            output.append(nums[myDeque[0]])
            leftPointer += 1

        rightPointer += 1

    return output


myArray = [1, 3, -1, -3, 5, 3, 6, 7]
print(maxSlidingWindow(myArray, 3))
