def amount(A, S):
    A.sort()

    res = []
    def backtrack_helper(cur, pos, S):
        if S == 0:
            res.append(cur.copy())
        if S <= 0:
            return

        prev = -1
        for i in range(pos, len(A)):
            if A[i] == prev:
                continue
            cur.append(A[i])
            backtrack_helper(cur, i+1, S-A[i])
            cur.pop()
            prev = A[i]

    backtrack_helper([], 0, S)
    return res

print(amount([11,1,3,2,6,1,5], 8))