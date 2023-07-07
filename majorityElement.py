def majorityElement(nums: list[int]) -> int:
    """
    define a dictionary, and add elements with their frequency in the dic
    then simply return the key which has value > length / 2 of array
    """

    freqBucket = {}

    for i in nums:
        if i not in freqBucket:
            freqBucket[i] = 1
        else:
            freqBucket[i] += 1

    for k, v in freqBucket.items():
        if v > len(nums) / 2:
            return k

    return 2


def majorityElementNew(nums: list[int]) -> int:
    major = nums[0]
    count = 1

    for i in range(1, len(nums)):
        if count == 0:
            count += 1
            major = nums[i]
        elif nums[i] == major:
            count += 1
        else:
            count -= 1

    return major


myList = [3, 2, 3]
myNewList = ['A', 'A', 'A', 'C', 'C', 'B', 'C', 'A', 'B']
majorityElementNew(myNewList)
majorityElement(myList)
