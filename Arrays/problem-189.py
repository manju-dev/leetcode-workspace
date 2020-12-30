# Problem 189: Rotate Array
class Solution:
    # Approach 1: Brute Force
    def rotate1(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        foo = None
        previous = None
        for i in range(k):
            previous = nums[len(nums)-1]
            for j in range(len(nums)):
                foo = nums[j]
                nums[j] = previous
                previous = foo

    # Approach 2: Using Extra Array
    def rotate2(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        foo = nums.copy()
        arrayLength= len(nums)
        for i in range(arrayLength):
            index = (i+k) % arrayLength
            foo[index] = nums[i]
        for j in range(arrayLength):
            nums[j] = foo[j]

    # Approach 3: Using Cyclic Replacements
    def rotate3(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        count = 0
        for i in range(len(nums)):
            if count >= len(nums):
                break
            current = i
            previous = nums[i]
            while True:
                next = (current + k) % len(nums)
                temp = nums[next]
                nums[next] = previous
                previous = temp
                current = next
                count += 1
                if(i == current):
                    break

    # Approach 4: Using Reverse
    def rotate4(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)

    def reverse(self, nums, start, end) -> None:
        while (start < end):
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    # Approach 5: Using Reverse (Built-in)
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]

# Test
solution = Solution()
# Expected: [5,6,7,1,2,3,4]
nums = [1,2,3,4,5,6,7]
solution.rotate(nums, 3)
print(nums)