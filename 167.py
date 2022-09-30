def twoSum(numbers: list[int], target: int) -> list[int]:
    l = 0
    r = len(numbers)-1

    while (l < r):
        sum = numbers[l] + numbers[r]
        if sum == target:
            return [l+1, r+1]
        elif sum > target:
            r -= 1
        else:
            l += 1

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))