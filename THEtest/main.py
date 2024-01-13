#!/usr/bin/env python3
import random as r 

# generating random numbers for calculation 
def genNum(x): 
    li = []
    i = 0
    while i < x: 
        li.append(r.randint(0,100))
        print(li[i])
        i += 1

def getAns():
    Ans = int()
    print(type(Ans))
    Ans = input("Please give numerical information:  \n ")
    Ans = int(Ans)
    print(type(Ans))

genNum(10)
getAns()


# this only works for the main file when you import stuff into it 
# if "__name__" == "__main__":
#     print("nothing")
#     genNum(4)