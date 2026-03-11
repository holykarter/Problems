
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # need ot use tow pointer 
        b = len(nums)
       
        for i in range(b):  # first boundary and second boundary problems   
            c = b - 1 
            while c  > 0:          
                if  (i, nums[i]) != (c, nums[c]):
                    if nums[i] + nums[c] == target:
                        return [i, c]
                c -= 1
        return None

s = Solution()

#unit test
nums = [1,3,4,2]
target = 6
a = s.twoSum(nums, target)
print(a)



'''
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: B
ecause nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

# idea for testing 
see how the c-1 in the condition and the c-1 in the loop affect 
the index
>>> a = list(range(10))
>>> c = len(a)
>>> for i in range(len(a)):
...     while c > 0:
...         if i != c - 1:
...             a[c - 1]
 
'''
