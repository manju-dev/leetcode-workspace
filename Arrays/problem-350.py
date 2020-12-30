# 350. Intersection of Two Arrays II
class Solution:
    # Approach 1: Iterate over two lists
    def intersect1(self, nums1, nums2) -> List[int]:
        intSection = []
        for i in nums1:
            for j in nums2:
                if i == j:
                    intSection.append(i)
                    nums2.remove(j)
                    break
        return intSection
    
    # Approach 2: Iterate over two lists with 'in'
    def intersect2(self, nums1, nums2)  -> List[int]:
        intSection = []
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                intSection.append(i)
        return intSection
    
    # Approach 3:
    def intersect3(self, nums1, nums2) :
        intSection = []
        foo = {}
        for i in nums1:
            foo[i] = foo.get(i, 0) + 1
        for j in nums2:
            if (j in foo) and foo.get(j, 0) > 0:
                intSection.append(j)
                foo[j] = foo.get(j) - 1
        return intSection
    
    # Approach 4:
    def intersect4(self, nums1, nums2) :
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())
    
    # Approach 5:
    def intersect(self, nums1, nums2) :
        nums1.sort() 
        nums2.sort()
        idx1 = 0
        idx2 = 0
        output = []

        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] > nums2[idx2]:
                idx2 += 1
            elif nums1[idx1] < nums2[idx2]:
                idx1 += 1
            else:
                output.append(nums1[idx1])
                idx1 += 1
                idx2 += 1

        return output

# Test
solution = Solution()
# Expected: 1
nums1 = [2,3,2,3,6,1,6]
nums2 = [2,2,3,6]
print(solution.intersect(nums1, nums2))