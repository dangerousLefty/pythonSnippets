class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insert_index = len(nums1) - 1  # 5
        ptr1 = m - 1
        ptr2 = n - 1

    # if the nums1 array is empty, then simply add all elements from nums2 to nums1
        while ptr2 >= 0:
            # print("hello")
            if ptr1 == -1:
                while ptr2 >= 0:
                    nums1[insert_index] = nums2[ptr2]
                    insert_index -= 1
                    ptr2 -= 1

            else:
                if nums2[ptr2] > nums1[ptr1]:
                    nums1[insert_index] = nums2[ptr2]
                    ptr2 -= 1
                else:
                    nums1[insert_index] = nums1[ptr1]
                    ptr1 -= 1

                insert_index -= 1


solution1 = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

solution1.merge(nums1, 3, nums2, 3)
