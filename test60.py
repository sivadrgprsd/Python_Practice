import re
str= ["Hello","DevOps","Python"]

result= str[0] + " " + str[1] + " " + str[2]

search=re.search("DevOps", result)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")    

print(len(result))
print(result.upper())
print(result.lower())
print(result.replace("DevOps","Pega"))  
print(result.split())
print("Modified text:", re.sub(str[2], str[0], result))
print("split_result:",re.split(str[1], result))

test

