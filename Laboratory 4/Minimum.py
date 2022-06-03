def Min(A):
    if len(A) == 0:
        return None
    if len(A) == 1:
        return (A[0])
    return min(A[0], Min(A[1:]))


def Max(A):
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]
    return max(A[0], Max(A[1:]))

# Driver Code

print(Max([2,4,6,3]))
print(Min([2,4,6,3]))