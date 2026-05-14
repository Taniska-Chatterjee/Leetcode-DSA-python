#class Solution:
    #def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]
        #rec = []
        #for x in nums1:
            #index = nums2.index(x)
            #next_greater = -1
            #for j in range(index + 1, len(nums2)):
               # if nums2[j] > x:
                  #  next_greater = nums2[j]
                 ## rec.append(next_greater)

       # return rec



class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        mapp = {}
        stack = []

        for x in nums2:
            while stack and x > stack[-1]:
                smaller_elemnt = stack.pop()
                mapp[smaller_elemnt] = x
            stack.append(x)

        return [mapp.get(x, -1)for x in nums1]

    