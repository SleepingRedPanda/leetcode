def sortedSquares( nums: list[int]) -> list[int]:
    # output_arr = [0] * len(nums)
    # l, r = 0, len(nums) - 1
    # while l <= r:
    #     left, right = abs(nums[l]), abs(nums[r])
    #     if left > right:
    #         output_arr[r-l] = left**2
    #         l += 1
    #     else:
    #         output_arr[r-l] = right**2
    #         r -= 1
    # return output_arr

    l, r = 0, len(nums)-1
    output_arr = [0]*len(nums)

    while l < r:
        first, last = abs(nums[l]), abs(nums[r])

        if first > last:
            output_arr[r-l] = first**2
            l += 1
        else:
            output_arr[r-l] = last**2
            r -= 1
    return output_arr



print(sortedSquares([-4,-1,0,3,10]))
