import random
m=list(range(0,9))
n=random.sample(m,k=4)
print(n)
store=n
k=1
chance=5
while k<chance:
    guess=input("enter your guess the number-")
    i=0
    list1=[]
    while i<len(guess):
        s=guess[i]
        list1.append(int(s))
        i=i+1
    print(list1)
    store1=list1
    j=0
    index=0
    count1=0
    count2=0
    while j<len(store1):
        index=0
        while index<len(store):
            if j==index:
                if store1[j]==store[index]:
                    count1=count1+1
            elif store1[j]==store[index]:
                count2=count2+1
            index=index+1
        j=j+1
    print("bull",count1)
    print("cow",count2)
    if store1==store:
        print("you own the game--")
        break
    else:
        print("you guess the game wrong--")
        print("you have",chance-k,"chance")
    user=input("do you want to play again this game yes or no--")
    if user=="yes":
        print(" ")
        k=k+1
    else:
        print(" ok,you lose the game")
        break
    print("you lose your chance--")







