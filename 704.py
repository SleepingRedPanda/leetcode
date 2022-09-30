def search(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif target > nums[m]:
            l = m + 1
        else:
            r = m - 1
    return -1

print(search([-1,0,3,5,9,12],9))