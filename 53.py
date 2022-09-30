def maxSubArray(nums: list[int]) -> int:
    cur_sum = max_sum = nums[0]
    for num in nums[1:]:
        cur_sum = max(num, cur_sum + num)
        max_sum = max(cur_sum, max_sum)
    return max_sum


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))