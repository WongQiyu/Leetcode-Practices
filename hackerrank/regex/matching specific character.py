Regex_Pattern = r'^[1-3][0-2][xs0][30Aa][xsu][.,]$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

#[] is a character class e.g. in index 0 can be 1,2,3