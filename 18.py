def fourSum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    quadruplets = []
    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-2):
            if j > i+1 and nums[j] == nums[j - 1]:
                continue
            twoSum(nums, target, i, j, quadruplets)
    return quadruplets

def twoSum(nums: list[int], target: int, first: int, second: int, quadruplets:list[int]) -> list[list[int]]:
    l = second + 1
    r = len(nums) - 1
    res = []
    while l < r:
        if target == nums[l] + nums[r]:
            res.append([nums[l], nums[r]])
            l += 1
            r -= 1
            while l < r and nums[l] == nums[l - 1]:
                l += 1
            while l < r and nums[r] == nums[r + 1]:
                r -= 1
        elif target > nums[l] + nums[r]:
            l += 1
        else:
            r -= 1
    return res

nums = [2,3,4]
target = 6
print(twoSum(nums, target))