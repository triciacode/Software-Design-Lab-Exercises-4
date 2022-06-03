def multiply(m,n):
    if(n <= 1):
        return m
    else:
        return m + multiply(m,n - 1)
multiply = multiply(14,24)
print(multiply)