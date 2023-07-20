#PROGRAM1
import re
txt="The rain in Spain"
#Check if the string ends with "Spain":
x=re.findall("Spain\Z",txt)
print(x)
if x:
    print("Yes, there is a match!")
else:
    print("No match")
print("\n")

#PROGRAM2- Match() Function
import re
string="She sells sea shells on the sea shore"
pattern1= "sells"
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

#PROGRAM3(Search Function)
import re
string="She sells sea shells on the sea shore"
pattern1="sells"
if re.search(pattern1,string):
    print("Match Found")
else:
    print(pattern, "is not present in the string")
print("\n")

#PROGRAM4
import re
pattern=r"[a-zA-Z]+ \d+"
matches=re.findall(pattern, "LXI 2013,VXI 2015,VDI 20104, Maruti Suzuki Cars in India")
for match in matches:
    print(match, end=" ")
print("\n")

#PROGRAM4
import re
line="pet:cat i love cats pet:cow i love cows"
match=re.findall(r"pet:\w\w\w",line)
print(match)
print("\n")

#PROGRAM5- The sub() Function
import re
string="She sells sea shells on the sea shore"
pattern="Sea"
repl="ocean"
new_string=re.sub(pattern,repl,string,1)
print(new_string)


