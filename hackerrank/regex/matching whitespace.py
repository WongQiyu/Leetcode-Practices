#\s matches any whitespace character [ \r\n\t\f ]
# \S matches any non-white space character.
'''
You have a test string . Your task is to match the pattern XXxXXxXX
Here,  denotes whitespace characters, and  denotes non-white space characters.

'''

Regex_Pattern = r"(\S{2}\s){2}\S{2}"    # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())