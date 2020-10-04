def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    not_vowel = ''
    for i in s:
        for i not in vowels:
            not_vowel +=i
    return not_vowel


print(remove_vowels('hello world'))

