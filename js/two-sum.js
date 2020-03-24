function twoSum(nums, target) {
    let hash = {};

    for(let i in nums) {
        let r = target - nums[i]
        
        if(hash[r]) {
            return [hash[r], i]
        }
        
        hash[nums[i]] = i
    }
}

console.log(twoSum([2,7,11,15], 9))