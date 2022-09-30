def findMaxAverage(nums: list[int], k: int) -> float:
    max_sum = 0
    for i in range(k):
        max_sum += nums[i]
    curr_sum = max_sum
    for i in range(1,len(nums)-k+1):
        curr_sum = curr_sum - nums[i-1] + nums[i+k-1]
        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum / k

print(findMaxAverage([5], 1))