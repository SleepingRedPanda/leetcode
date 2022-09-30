def twoSum(nums: list[int], target: int) -> list[int]:
    l = 0
    r = len(nums) - 1
    res = []
    while l < r:
        if target == nums[l] + nums[r]:
            res.append(l)
            res.append(r)
            l += 1
            r -= 1
            while l<r and nums[l] == nums[l-1]:
                l += 1
            while l<r and nums[r] == nums[r+1]:
                r -= 1
        elif target > nums[l] + nums[r]:
            l += 1
        else:
            r -= 1
    return res


nums = [3,2,4]
target = 6
print(twoSum(nums, target))