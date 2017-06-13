import string
import random

def stretch(string, factor=2, letters=(string.ascii_lowercase)+(string.ascii_uppercase)):
    NewString = ""
    for character in string:
        if letters.count(character) >0:
            NewString = NewString + (factor*character)
        else:
            NewString = NewString + character
    return NewString

flip = random.randrange(0,2)
randamount = random.randrange(0,52+1)
randfactor = random.randrange(-1,11)
randletter = 0
randlist = ""

for amount in range(0, randamount+1):
    randletter = chr(random.randrange(65,123))
    if (ord(randletter)>=91) and (ord(randletter)<=96):
        if flip == 0:
            randletter = chr(random.randrange(65,91))
        else:
            randletter = chr(random.randrange(97,123))
    randlist = randlist+randletter

for character in randlist:
    if randlist.count(character) >1:
        index = randlist.find(character)
        randlist = randlist[:index] + randlist[index+1:]

minord = 125
maxord = 60
for character in randlist:
    if ord(character) >= maxord:
        maxord = ord(character)
    elif ord(character) <= minord:
        minord = ord(character)

for i in range(maxord+1):
    for character in randlist:
        if ord(character) == (minord+i):
            index = randlist.find(character)
            randlist = randlist[:index]+randlist[index+1:]+character

print("Of these letters:", randlist, "("+str(len(randlist)), "letter(s))")
print("There will be this many of each letter chosen:", randfactor)
print(stretch("Jim Vargas", randfactor, randlist))
