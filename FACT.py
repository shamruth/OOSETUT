def fact(n):
    if n==1:
        return 1
    else:
        return(n * fact(n-1))
x=5
result=fact(x)
print(result)
