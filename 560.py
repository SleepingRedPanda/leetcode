def subarraySum(nums: list[int], k: int) -> int:
    count = 0
    h = {0:1}
    cur_sum = 0
    for i in nums:
        cur_sum += i
        diff = cur_sum - k

        count += h.get(diff, 0)
        h[cur_sum] = 1 + h.get(cur_sum, 0)

    return count

print(subarraySum([1,2,3], 3))