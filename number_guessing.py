import random as rd
num=rd.randint(1,10)
chances=4
while(chances>1):
    n=int(input("enter number between 1-100"))
    if(n==num):
        print("u guess the correct number");
        break;
    else:
        print("try another time");
        chances=chances-1;
else:
    print("ur game is over")