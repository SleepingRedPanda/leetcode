def pivotIndex(nums: list[int]) -> int:
    l = 0
    right_sum = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        left_sum += nums[i]
        if right_sum == left_sum:
            return i
        right_sum -= nums[i]

print(pivotIndex([-1,-1,0,1,1,0]))