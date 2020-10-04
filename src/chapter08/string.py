fruit = 'banana'
x = fruit[1]
print(x)
print(list(enumerate(fruit)))

ix = 0
while ix < len(fruit):
    letter = fruit[ix]
    print(letter)
    ix += 1

for i in fruit:
    print(i)

prefix = 'JKLMNOPQ'
suffix = 'ack'

for i in prefix:
    print(i + suffix)

print(fruit [3:-2])

greeting = "hello world"
new_greeting = 'y' + greeting
print(new_greeting)
print(new_greeting(2,4))