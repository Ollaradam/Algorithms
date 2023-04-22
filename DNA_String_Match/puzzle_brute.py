def puzzle_brute(n):
    if (n<=0):
        return 0
    if (n==1):
        return 1
    if (n==2):
        return 2

    return puzzle_brute(n-1) + puzzle_brute(n-2)

n=10
print(puzzle_brute(n))