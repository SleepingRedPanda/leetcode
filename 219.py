def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    d = {}

    for i, v in enumerate(nums):
        if v in d and (i - d[v]) <= k:
            return True
        d[v] = i
    return False



print(containsNearbyDuplicate([1,0,1,1],1))