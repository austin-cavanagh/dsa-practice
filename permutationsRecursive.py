# Time: O(n^2 * n!)
def permuatationsRecursive(nums):
    return helper(0, nums)

def helper(i, nums):
    if i == len(nums):
        return [[]]
    
    resPerms= []
    perms = helper(i + 1, nums)

    for p in perms:
        for j in range(len(p) + 1):
            pCopy = p.copy()
            pCopy.insert(j, nums[i])
            resPerms.append(pCopy)
    
    return resPerms