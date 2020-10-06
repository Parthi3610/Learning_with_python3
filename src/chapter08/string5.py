s1 = "hello all, today is {0}"
print(s1.format("thursday"))

name = "parthi"
age = 25
s1 = "this is {1} and age {0}"
print(s1.format(age,name))

n1 = 4
n2 = 5

s1 = ("5**3 is = {0} and {1} * {2} = {3:f}").format(5**3, n1, n2, n1*n2)
print(s1)

n1 = "Sachin"
n2 = "Ramesh"
n3 = "Tendulkar"

print("Pi value is {0:.3f}".format(3.14596))
print("first name {0:>15}|| middle name {1:^15}|| last name {2:<15}".format(n1, n2, n3))
print("covert decimal value {0} to bin value {0:b}".format(1234))