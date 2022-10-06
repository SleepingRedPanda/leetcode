import math

def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()
    res = 0
    diff = math.inf
    n = len(nums)
    for i in range(n):
        left = i + 1
        right = n - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if abs(target - curr_sum) < diff:
                diff = abs(target - curr_sum)
                res = curr_sum
            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return target
    return res


