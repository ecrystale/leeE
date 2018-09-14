'''
Ingeborgwerner-Emily Lee, Ahnaf Kazi
SoftDev1 pd6
K#6 -- Stl/O:Divine your Destiny!
2018-09-13
'''  

import random

#initializes dictionary
occ={}

#finds position of comma
def first(word):
    place=0
    final=0
    count=0
    for char in word:
        if char=='"':
            count+=1
        if count!=1:
            if char==",":
                final=place
            else:
                place+=1
        else:
            place+=1
    return final

file=open("occupations.csv","r")

def isnum(number):
    try:
        float(number)
        return True
    except:
        return False

#enumerates dictionary
for line in file:
    place=first(line)
    if(isnum(line[place+1:len(line)-1])):
        occ[line[0:place]]=float(line[place+1:len(line)-1])
        
full=float(occ['Total'])
occ.pop('Total')
#print(occ)

def randomOcc():
    ran = random.uniform(1,full)
    count=0
    for key in occ:
        count+=occ[key]
        if(count>=ran):
            return key

def test():
    testDict = dict.fromkeys(occ, 0);
    for x in range(0, 1000):
        testDict[randomOcc()]+=.1;
    print(testDict)
    print("\n")
    print(occ)
    for key in testDict:
        print(key+ ": " + str(testDict[key]-occ[key]))

#test()
print(randomOcc())
