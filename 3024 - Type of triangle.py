nums = [1,2,2]

if ((nums[0]+nums[1])>nums[2] and (nums[0]+nums[2])>nums[1] and (nums[1]+nums[2])>nums[0]):
    if len(set(nums))== 1:
        print("equilateral")
    elif len(set(nums))==2:
        print('isoceles')
    else:
        print('scalene')
else:
    print('none')