class Solution:
    def twoSum(self, nums, target: int):
        hash = {}
        
        for index, num in enumerate(nums):
            result = target - num
            
            if result in hash:
                return [hash.get(result), index]
            
            hash[num] = index

print((Solution()).twoSum([2,7,11,15],9))