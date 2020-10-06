layout = "{0:>4}{1:>6}{2:>8}{3:>10}{4:>12}{5:>12}"

print(layout.format("i","i**2","i**3","i**4","i**5", "i**9"))

for i in range(1,10):
    print(layout.format(i,i**2, i**3, i**4, i**5, i**9))
