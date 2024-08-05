import sys

try:
  num1= int(sys.argv[1])
  num2= int(sys.argv[3])
  operator= sys.argv[2]
except ValueError:
    print("provide valid data")

def add():
    x= num1+num2
    return x
def sub():
    x= num2-num1
    return x
def div():
    x=num2/num1
    return x

if operator== "add":
    print("result:",add())
elif operator=="sub":
    print("result:",sub())
elif operator=="div":
    print("result:",div())
else:
        print("invalid")
