function twoSum(nums, target) {
    let hash = {};

    for(var index in nums) {
        let result = target - nums[index]

        if(hash[result]) {
            return [hash[result], index]
        }

        hash[nums[index]] = index
    }
}

console.log(twoSum([2,7,11,15], 9))