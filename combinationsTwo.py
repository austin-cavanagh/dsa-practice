# Time: O(k * C(n, k))
def combinationsTwo(n, k):
    combs = []
    helper(1, [], combs, n, k)
    return combs

def helper(i, curComb, combs, n, k):
    if len(curComb) == k:
        combs.append(curComb.copy())
        return
    
    if i > n:
        return
    
    for j in range(i, n + 1):
        curComb.append(j)
        helper(j + 1, curComb, combs, n, k)
        curComb.pop()