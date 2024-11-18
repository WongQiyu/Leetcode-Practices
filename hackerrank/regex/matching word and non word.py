Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

'''
\W matches any non-word character.
Non-word characters include characters other than alphanumeric characters (A-Z, a-z  and 0-0) and underscore (_).
The expression \w will match any word character.
'''