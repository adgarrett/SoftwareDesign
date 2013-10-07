def recurse(n, s):
    if n == 0:
        return s
    else:
        return recurse(n-1, n+s)

print recurse(4, 0)
