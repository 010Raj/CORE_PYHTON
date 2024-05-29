import re
TXT = "The Rain in Spain"
x = re.search("The Rain", TXT)
if (x):
    print("YES ! We have a match !")
else:
    print("No Match")

# findall():this function returns the list of containing all matches

str = "The Rain in Spain"
x = re.findall("in",str)
print(x)

# search(): The search() function searches the string for a match,and returns a match obj. if there is a match

x = re.search('Rain', TXT)
if x:
    print("pattern found inside the string")
else:
    print("pattern not found")

# split():this function returns a list where the string has been split at each match

x = re.split("\s", TXT)
print(x)

# sub(): this function replaces the matches with the text of your choice

x = re.sub("\s",",",str,)
print(x)
