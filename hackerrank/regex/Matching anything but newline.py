regex_pattern = r"^(...\.){3}...$"	# Do not delete 'r'.
# ^ anchors start
# \.: match .
# ... match any three char
#$ end


import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())