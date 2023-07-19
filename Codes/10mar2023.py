#PROGRAM1
import re
txt="The rain in Spain"
#Find all the lower case characters alphabetically between "a" and "m"
x=re.findall("[a-m]",txt)
print(x)
print("\n")

#PROGRAM2
import re
txt="That will be 59 dollars"
#Find all digit character"
x=re.findall("\d",txt)
print(x)
print("\n")

#PROGRAM3
import re
txt="hello planet"
#Search for a sequence that starts with "he", followed bytwo(any) characters, and an"o":
x=re.findall("he..o",txt)
print(x)
print("\n")

#PROGRAM4
import re
#Check if the string starts with "hello":
x="hello planet"
#Check if the string starts with 'hello':
x=re.findall("^hello",txt)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")
print("\n")

#PROGRAM5
txt="hello planet"
#Check if the string ends with 'planet'
x=re.findall("planet$",txt)
if x:
    print("Yes, the string ends with 'planet'")
else:
    print("No match")
print("\n")

#PROGRAM6
import re
txt="hello planet"
#Search for a sequence that starts with "he", followed by 0 or more (any) characters, and an "o":
x=re.findall("he.*o",txt)
print(x)
print("\n")

#PROGRAM7
import re
txt="hello planet"
#Search for a sequence that starts with "he", followed by 1 or more (any) characters, and an "o":
x=re.findall("he.+o",txt)
print(x)
print("\n")

#PROGRAM8
import re
txt="hello planet"
#Search for a sequence that starts with "he", followed exactly 2(any) characters, and an "o":
x=re.findall("he.{2}o",txt)
print(x)
print("\n")

#PROGRAM9
import re
txt="hello planet"
#Search for a sequence that starts with "he", followed by 0 or 1 (any) character, and an "o":
x=re.findall("he.?o",txt)
print(x)
print("\n")

#PROGRAM10
import re
txt="The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x=re.findall("falls|stays",txt)
print(x)
if x:
    print("Yes, there is atleast one match!")
else:
    print("No Match")
print("\n")

#PROGRAM11
import re
txt="The rain in Spain"
#Check if the string starts with "The":
x=re.findall("\AThe",txt)
print(x)
if x:
    print("Yes, there is a match!")
else:
    print("No Match")
print("\n")

#PROGRAM12
import re
txt="The rain in Spain"
#Check if "ain" present at the beginning of a Word:
x=re.findall(r"\bain",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
print("\n")

#PROGRAM13
import re
txt="The rain in Spain"
#Check if "ain" present at the end of a Word:
x=re.findall(r"ain\b",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
print("\n")

#PROGRAM14
import re
txt="The rain in Spain"
#Check if "ain" present, but NOT at the beginning of a Word:
x=re.findall(r"\Bain",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
print("\n")

#PROGRAM15
import re
txt="The rain in Spain"
#Check if the string contains any digits (numbers from 0-9):
x=re.findall("\d",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
print("\n")

#PROGRAM15
import re
txt="The rain in Spain"
#Return a match at every no-digit character:
x=re.findall("\D",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
print("\n")

#PROGRAM15
import re
txt="The rain in Spain"
#Return a match at every white-space character:
x=re.findall("\s",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
print("\n")

#PROGRAM16
import re
txt="The rain in Spain"
#Return a match at every NON white-space character:
x=re.findall("\S",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
print("\n")

#PROGRAM17
import re
txt="The rain in Spain"
#Returns a match at every word character (characters from a to Z, digits from 0-9, and the underscore_ character):
x=re.findall("\w",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
print("\n")

#PROGRAM18
import re
txt="The rain in Spain"
#Return a match at every NON word character (characters NOT between a and Z, like "!","?" white-space etc):
x=re.findall("\W",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
print("\n")
