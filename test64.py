import re
import sys
arn = "abc/fgh"
print(arn.split("/"))


number1 = 5
number2 = 6
tot = number1+number2
print('exact amount', tot)


text = "vaishali is good"
pattern = "vaishali"
match = re.match(pattern,text)
if match:
    print("match found:",match.group())
else:
    print("no mactch found")

def add(n1,n5):
    n3=n1 + n5
    return n3

n1 = int(sys.argv[1])
operation = sys.argv[2]
n2 = int(sys.argv[3])
if operation == "add":
    y = add(n1, n2)
    print(y)

