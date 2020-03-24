class Solution:
    def twoSum(self, nums, target: int):
        hash = {}
        
        for index, num in enumerate(nums):
            result = target - num
            
            if result in hash:
                return [hash.get(result), index]
            
            hash[num] = index

print((Solution()).twoSum([2,7,11,15],9))


## Faster
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for k in range(len(nums)):
          r = target-nums[k]

          if dict.get(r) is not None:
            return [dict.get(r), k]

          dict[nums[k]] = k
