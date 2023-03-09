def twoSum(lst, target):
    n = len(lst)

    for i in range(n-1):
        for j in range(i+1, n):
            if lst[i] + lst[j] == target:
                return [i, j]

