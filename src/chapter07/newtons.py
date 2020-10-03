def sqrt(n):
    approx = n/2
    count = 0
    while True:
        better = (approx + n/approx)/2.0
        count += 1
        if abs(approx - better) < 0.001:
            return (better, count)
        approx = better

print(sqrt(25))
#print(int(sqrt(45)), count)

