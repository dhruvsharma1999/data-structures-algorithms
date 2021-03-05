"""
given a list of number and a target value, find if the list have two number whose sum 
is equal to the target value, no repitition is allowed"""

nums = [1,3,11,2,3,4,5,7]
target = 13 

def two_digits(nums, target):
    if len(nums) <= 1:
        return False

    aux_dict = {} 
    for i in range(len(nums)): 
        if nums[i] in aux_dict:
            return [aux_dict[nums[i], i]]

        else:
            aux_dict[target - nums[i]] = i 


    