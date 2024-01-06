#!/usr/bin/env python3
import random as r 

# generating random numbers for calculation 
def genNum(x): 
    li = []
    i = 0
    while i < x: 
        li.append(r.randint(0,100))
        i += 1
    print(li)
    
genNum(4)

# this only works for the main file when you import stuff into it 
# if "__name__" == "__main__":
#     print("nothing")
#     genNum(4)