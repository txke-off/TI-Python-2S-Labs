# O(1)
def const(a):
    return a[0] if a else None

# O(n)
def linear(a):
    total = 0
    for i in a:
        total += i
    return total

# O(n^2)
def quadratic(a):
    result = []
    for i in a:
        for j in a:
            result.append(i+j)
    return result

# O(n^3)
def cubic(a):
    result = []
    for i in a:
        for j in a:
            for k in a:
                result.append(i*j*k)
    return result
