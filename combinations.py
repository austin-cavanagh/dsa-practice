# Given n numbers (1 - n), return all possible combinations of size k
# Time: O(k * 2^n)

def combinations(n, k):
    combs = []
    helper(1, [], combs, n, k)
    return combs

def helper(i, curComb, combs, n, k):
    if len(curComb) == k:
        combs.append(curComb.copy())
        return
    
    if i > n:
        return
    
    # Decision to include i
    curComb.append(i)
    helper(i + 1, curComb, combs, n, k)
    
    # Decision not to include i
    curComb.pop()
    helper(i + 1, curComb, combs, n, k) 