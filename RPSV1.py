#in arr[] 1 is rock 2 is paper and 3 is scissors
import random as r
x=None
print("This a rock paper sccisors game")
while x!="n":
    x=input("Rock, Paper or Scissors= ").lower()
    if x== 'rock':
        x=1
        arr=[2,3]
        c1=r.choice(arr)
        if c1==2:
            print("I picked Paper and Paper beats Rock!")
        else:
            print("I picked Scissors, and Scisors loses to Rock!")
    elif x=='paper':
        x=2
        arr=[1,3]
        c1=r.choice(arr)
        if c1==1:
            print("I picked Rock, and Rock loses to Paper!")
        else:
            print("I picked Scissors, and Scissors beats Paper")
    else:
        x=3
        arr=[1,2]
        c1=r.choice(arr)
        if c1==1:
            print("I picked Rock, and Rock beats Scissors!")
        else:
            print("I picked Paper, and Paper loses to Scissors!")
    x=(input("Would you like to play again?(Y/n)= ")).lower()
print("Ok! Thanks for play")