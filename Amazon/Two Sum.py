'''
1. Two Sum
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Runtime: 58 ms, faster than 77.69% of Python3 online submissions for Two Sum.
Memory Usage: 15.3 MB, less than 54.92% of Python3 online submissions for Two Sum.
'''
import heapq
nums = [2, 7, 11, 15]
target = 9
heap = list(nums)
heapq.heapify(heap)
print(heap)
middle = int(len(nums) / 2)
print(middle)
hash_table = dict()


def two_sum(nums, target):
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_table:
            return (i, hash_table[complement])
        else:
            hash_table[nums[i]] = i
    return None


print(two_sum(nums, target))
