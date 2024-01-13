#!/usr/bin/env python3
import random as r 

# generating random numbers for calculation 
def genNum(x): 
    li = []
    i = 0
    while i < x: 
        li.append(r.randint(0,100))
        #print(li[i])
        i += 1
    return li

# getting user input 
def getAns():
    Ans = int()
    print(type(Ans))
    Ans = input("Please give numerical information:  \n ")
    Ans = int(Ans)
    print(type(Ans))
    return Ans

# creating the question
def creQue():
    liste = genNum(4)
    print(liste)
    print("Add", liste[0], "and", liste[1])
    answer = input()
    answer = int(answer)
    corAnswer = liste[0] + liste[1]
    if answer == corAnswer:
        print("correct!")
    else:
        print("It's actually", corAnswer)
    


#genNum(4)
#getAns()
creQue()

# this only works for the main file when you import stuff into it 
# if "__name__" == "__main__":
#     print("nothing")
#     genNum(4)