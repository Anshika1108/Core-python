import re

txt = "The rain in Spain"


x = re.search('world',txt)

if x:
    print("Pattern found inside the string")
else:
    print("Pattern not found")

y = re.search('rain',txt)

if y:
    print("Pattern found inside the string")
else:
    print("Pattern not found")