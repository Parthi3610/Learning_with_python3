b = [1,2,3,4]
a = [5,6,7,"hello"]
print(a+b)
print(a)
print(b)
print(b,a)

c = a*3
print(c)
print(c[7])

xs = [1,2,3,4,5]

for (i,val) in enumerate(xs):
    xs[i] = val*2
    print(i,val)

mx = [[1,2,3],[4,5,6],[7,8,9]]

print(mx[2])
print(mx[1][0])
