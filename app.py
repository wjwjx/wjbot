import random

def Convert(string):
    li = list(string.split(" "))
    return random.choice(li)
 
 
# Driver code
str1 = input()
print(Convert(str1))
