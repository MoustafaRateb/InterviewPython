def rob(nums):
    robs =[nums[0], max(nums[0],nums[1])]

    for i in range(2,len(nums)):
        robs.append(max(robs[i-1],nums[i]+robs[i-2]))
    
    return max(robs)
