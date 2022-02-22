import random
fp= open ('words.txt' , 'r')
words=fp.readlines()

word = random.choice(words)[:-1]

guesses=[]
error_left=len(word)
done =False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_",end=" ")
    print("")
    
    guess = input(f"guesses left {error_left}, Next Guess:")
    guesses.append(guess)
    if guess.lower() not in word:
        error_left-=1
        if error_left==0:
            break;
            
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False
        
if done:
    print(f"you Guess successfully and the word is {word}")
else:
    print("your game is over")