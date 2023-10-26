def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """                                                                                                             
    # for i in range(len(nums)):
    #     for k in range(i + 1, len(nums)):
    #         if nums[i] + nums[k] == target:
    #             return [i,k]
    # return -1
    hashmap = {}

    for i in range(len(nums)):
        answer = target - nums[i]
        if answer in hashmap:
            return [i, hashmap[answer]]
        hashmap[nums[i]] = i


def two_sum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        ans = target - num
        if ans in hash_map:
            return [i, hash_map[ans]]
        hash_map[num] = i
print(two_sum([2,7,11,15], 9))
