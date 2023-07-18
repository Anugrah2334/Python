#PROGRAM1(\-Backslash)
import re
s='geeks.forgeels'
#without using \
match=re.search(r'.',s)
print(match)
#using \
match=re.search(r'\.',s)
print(match)
print("\n")

#PROGRAM2
import re
string="She sells sea shells on the sea shore"
pattern1="sells"
if re.match(pattern1,string):
    print("Match Found")
else:
    print(pattern1, "is not present in the string")
pattern2="She"
if re.match(pattern2,string):
    print("Match Found")
else:
    print(pattern2, "is not present in the string")
print("\n")

#PROGRAM3
import re
txt="The rain in Spain"
#Find all lower case character alphabetically between "a" and "m"
x=re.findall("[a-m]",txt)
print(x)
print("\n")

import re
txt="That will be 59 dollars"
#Find all digit characters:
x=re.findall("\d",txt)
print(x)
print("\n")

import re
txt="hello planet"
#Search for a sequence that starts with "he",followed by two (any) characters, and an "o"
x=re.findall("he..o",txt)
print(x)
print("\n")

import re
txt="hello planet"
#Check if the string starts with 'hello'
x=re.findall("^hello",txt)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No Match")
print("\n")

import re
txt="hello planet"
#Check if the string ends with 'planet':
x=re.findall("planet$",txt)
if x:
    print("Yes, the string ends with 'planet'")
else:
    print("No Match")
print("\n")

import re
txt="hello planet"
#Search for a sequence that starts with "he", followed by 0 or more (any) characters, and an "o":
x=re.findall("he.*o",txt)
print(x)
print("\n")

import re
txt="hello planet"
#Search for a sequence that starts with "he", followed by 1 or more (any) characters, and an "o":
x=re.findall("he.+o",txt)
print(x)
print("\n")

import re
txt="hello planet"
#Search for a sequence that starts with "he", followed exactly 2(any) characters, and an "o":
x=re.findall("he.{2}o",txt)
print(x)
print("\n")

import re
txt="hello planet"
#Search for a sequence that starts with "he", followed by 0 or 1 (any) character, and an "o":
x=re.findall("he.?o",txt)
print(x)
print("\n")

import re
txt="The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x=re.findall("falls|stays",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No Match")
print("\n")



