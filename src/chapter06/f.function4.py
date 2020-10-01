import sys

def test(did_pass):
    '''print results of test'''
    linenum = sys._getframe(1).f_lineno #get caller's line number
    if did_pass:
        msg = ("test at line {0} ok.".format(linenum))
    else:
        msg = ("test at line {0} failed.".format(linenum))
    print(msg)


def test_suit():
    test(5+7 == 17)
    test(5+7 == 12)


test_suit()