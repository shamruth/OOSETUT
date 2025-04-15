def fact(n):
    if n==1:
        return 1
    else:
        return(n * fact(n-1))
print(f"FACTORIAL OF GIVEN NUMBER IS:{fact(int(input("Enter a number to find factorial")))}")
