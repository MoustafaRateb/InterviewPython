def maxSubArray(nums):

    # handle all negative scenario
    if max(nums) <= 0:
        return max(nums)

    # define var for maxSum = -10^4-1
    maxSum = (10 ** 4 + 1) * -1

    subArraySum = 0
    # loop on nums
    for num in nums:
        # sum adjacent positive nums and also sum adjacent negative nums
        subArraySum += num
        if subArraySum > maxSum:
            maxSum = subArraySum
        if subArraySum < 0:
            subArraySum = 0
    return maxSum


print(maxSubArray([1]))
