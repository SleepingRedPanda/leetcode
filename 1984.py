def minimumDifference(nums: list[int], k: int) -> int:
    nums = sorted(nums) # O(nlogN)
    l = 0
    r = k-1
    min_diff = float('inf')
    while r < len(nums):
        min_diff = min(min_diff, nums[r]-nums[l])
        l+=1
        r+=1
    return min_diff

nums = [9,4,1,7]
k = 2
print(minimumDifference(nums, k))