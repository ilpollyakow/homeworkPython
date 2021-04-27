n = input()
def recursive(n, m):
    if n == 1:
        return n
    if m == 1:
        return m
    else:
        return n+recursive(n + m)
    print(recursive)
