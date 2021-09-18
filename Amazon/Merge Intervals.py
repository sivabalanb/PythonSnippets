'''
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
'''
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals = [[1, 4], [0, 4]]
sorted_interval = sorted(intervals, key=lambda r: r[0])
output = []
print("sorted_invterval", sorted_interval)
for i in sorted_interval:
    if output and i[0] <= output[-1][1]:
        output[-1][1] = max(output[-1][1], i[1])
    # elif output i[0] 
    else:
        output.append(i)

print("output", output)
