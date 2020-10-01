def seq3np1(n):
    """function for printing 3*n + 1 based on even and odd"""
    while (n!=1):
        print(n,end=", ")
        if (n%2) == 0:
            n = n // 2
        else:
            n = (n*3)+1
    print(n,end=".\n")


seq3np1(5)
seq3np1(20)