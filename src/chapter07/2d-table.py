def table_2d(input):
    """print 2d table """
    for i in range(1, input):
        print(2*i, end='   ')


t = input("enter a value:")
table_2d(int(t))
