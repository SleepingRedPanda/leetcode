def threeSum(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    triplets = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            curr_sum = nums[i] + nums[l] + nums[r]

            if curr_sum == 0:
                triplets.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1

                while l < r and nums[l-1] == nums[l]:
                    l += 1
                while l<r and nums[r+1] == nums[r]:
                    r -= 1
            elif curr_sum < 0:
                l += 1
            else:
                r -= 1
    return triplets

print(threeSum([-1,0,1,2,-1,-4]))