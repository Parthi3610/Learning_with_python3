def count_digits(n):
    """ function to find the number of digits """
    count = 0
    n=abs(n)
    while n!=0:
        count += 1
        n = n // 10
    return count

n=-111112
a=count_digits(n)
print("number of digits " + str(n) + ": " + str(a))


