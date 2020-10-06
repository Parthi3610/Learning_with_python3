def find(str,ch):
    #find the char and str
    ix = 0
    while ix < len(str):
        if str[ix] == ch:
            return ix
        ix += 1
    return -1

print(find('hello world', 'o'))
print(find('hello world', 'y'))


def count_a(str,ch):
    count = 0
    for i in str:
        if i == ch:
            count+=1
    return count

print(count_a('hello world', 'o'))
print(count_a('hello world', 'l'))
print(count_a('hello world', 't'))

'''
def count_a(str,ch,start):
    ix = start
    if ix < len(str):
    
print(count_a('hello world', w,3)
'''