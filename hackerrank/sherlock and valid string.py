#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def isValid(s):
    c = Counter(s)
    val = c.values()
    small = min(val)
    big = max(val)
    if len(set(val)) > 2:
        return "NO"
    if small == big:
        return "YES"

    big_lst = len([i for i in val if i == big])
    small_lst = len(val) - big_lst

    if big -small == 1 and (big_lst ==  1 or small_lst == 1 ):
        return "YES"
    if small_lst == 1 and small == 1:
        return 'YES'

    return "NO"




if __name__ == '__main__':
    print(Counter("ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd"))
    #print(Counter("aabbc"))
    #print(isValid("aabbc"))
    # print(isValid("aabbccddeefghi"))
    # print(Counter("aabbccddeefghi"))
    # print(Counter("abcdefghhgfedecba"))
    # print(Counter("abcc"))
    # print(Counter("aabbcd"))
    # print(isValid("abcdefghhgfedecba"))
    # print(isValid("abcc"))
    # print(isValid("aabbcd"))
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
    '''
