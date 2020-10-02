
high = 7

def print_multiples(n, high):
    for i in range(1, high):
        print(n*i, end = "  ")
    print()


def print_mult_table(high):
    for i in range(1, high+1):
        print_multiples(i, i+1)

print_mult_table(high)


#print_mult_table(7)
