import re
txt = "The rain in Spain"

x = re.search("The rain",txt)
if (x):
    print("yes we have a match")

else:
    print("No match")

y = re.search("USA",txt)
if (y):
    print("yes we have a match")

else:
    print("No match")