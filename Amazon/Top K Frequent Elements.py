'''
347. Top K Frequent Elements
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Runtime: 108 ms, faster than 42.15% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.8 MB, less than 34.57% of Python3 online submissions for Top K Frequent Elements.
'''
from collections import Counter
import heapq
nums = [1, 1, 1, 2, 2, 3]
k = 2

# d = [k for k, v in sorted(
#     Counter(nums).items(), key=lambda item: item[1], reverse=True)]

# print((heapq.nlargest(k, d)))

f = [k for k, v in sorted(Counter(nums).items(),
                          key=lambda i:i[1], reverse=True)]
print(f)
print(f[:k])
