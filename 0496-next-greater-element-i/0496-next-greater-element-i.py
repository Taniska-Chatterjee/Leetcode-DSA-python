class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        rec = []

        for x in nums1:

          
            index = nums2.index(x)

            next_greater = -1

          
            for j in range(index + 1, len(nums2)):

                if nums2[j] > x:
                    next_greater = nums2[j]
                    break

            rec.append(next_greater)

        return rec



    