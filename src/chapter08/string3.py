"""
str = "hello world"
print(str.find('ll',1,3))
"""

import string


def remov_punc(str):
    not_punc = ""
    # punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for i in str:
        if i not in string.punctuation:
            not_punc += i
    return not_punc


print(remov_punc("sdsffhello @$@%^%*&#*& world"))
