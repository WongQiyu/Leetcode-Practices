Regex_Pattern = r'^\D[^aeiou][^bcDF]\S[^AEIOU][^.,]$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

#https://github.com/nathan-abela/HackerRank-Solutions