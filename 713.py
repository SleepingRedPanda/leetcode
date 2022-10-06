def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    if k <= 1: return 0
    prod = 1
    l = 0
    ans = 0
    for r, value in enumerate(nums):
        prod *= value
        while prod >= k:
            prod /= nums[l]
            l += 1
        ans += r - l + 1
    return ans

nums = [10,5,2,6]
k = 100

print(numSubarrayProductLessThanK(nums, k))