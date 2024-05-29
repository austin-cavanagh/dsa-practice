# Time: O(n * 2^n)
# Space: O(n)

def subsetsWithDuplicates(nums):
    nums.sort()
    subsets, curSet = [], []
    helper(0, nums, curSet, subsets)
    return subsets

def helper(i, nums, curSet, subsets):
    if i >= len(nums):
        subsets.append(curSet.copy())
        return
    
    # Decision to include nums[i]
    curSet.append(nums[i])
    helper(i + 1, nums, curSet, subsets)

    # Decision not to include nums[i]
    curSet.pop()
    while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        i += 1
    helper(i + 1, nums, curSet, subsets)