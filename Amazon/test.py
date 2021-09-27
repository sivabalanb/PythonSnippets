nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    hash_table = dict()
    for i in range(len(nums)):
        print("hash_table, i, nums", hash_table, i, nums)
        complement = target - nums[i]
        print("complement", complement)
        if complement in hash_table:
            return (i, hash_table[complement])
        else:
            hash_table[nums[i]] = i
    return None


print(twoSum(nums, target))
