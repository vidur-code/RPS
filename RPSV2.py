#in arr[] 1 is rock 2 is paper and 3 is scissors
w=0
l=0
d=0
arr=[1,2,3]
import random as r
x=None
print("This a rock paper sccisors game")
while x!="n":
    x=input("Rock, Paper or Scissors= ").lower()
    if x not in ["rock","paper","scissors"]:
        print("Invalid choice! Choose again")
        continue
    elif x== 'rock':
        x=1
        c1=r.choice(arr)
        if c1==2:
            print("I picked Paper and Paper beats Rock!")
            w=w+1
        elif c1==x:
            print("I also picked Rock, that makes this a Draw!")
            d=d+1
        else:
            print("I picked Scissors, and Scisors loses to Rock!")
            l=l+1
    elif x=='paper':
        x=2
        c1=r.choice(arr)
        if c1==1:
            print("I picked Rock, and Rock loses to Paper!")
            l=l+1
        elif c1==x:
                    print("I also picked Paper, that makes this a Draw!")
                    d=d+1
        else:
            print("I picked Scissors, and Scissors beats Paper")
            w=w+1
    elif x=='scissors':
        x=3
        c1=r.choice(arr)
        if c1==1:
            print("I picked Rock, and Rock beats Scissors!")
            w=w+1
        elif c1==x:
                    print("I also picked Scissors, that makes this a Draw!")
                    d=d+1
        else:
            print("I picked Paper, and Paper loses to Scissors!")
            l=l+1
    x=(input("Would you like to play again?(Y/n)= ")).lower()
if l==0:
    kdr=100
else:
    kdr=w/l
print("Ok! Thanks for playing,you played,",(w+l+d)," your win amount was",w,"loss amount was",l,"draw amount,",d,"and win/loss ratio was",round(kdr,2),"wins per loss")