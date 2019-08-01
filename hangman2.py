import time
#welcoming the user
name=input("what's your name?")
print("hello"+name,"time to play hangman")

#wait for a  1 second
time.sleep(1)
print("start guessing")
time.sleep(1)

#here we set the word

word="monika, darlo"

#create a variable with an empty value
guesses=" "

#determine the number of turns
turns=7
#create a while loop
#check if the turns are more than zero
while turns>0:
    #make a counter that starts with zero
    failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("__")
            failed+=1
    if failed==0:
        print("you won")
        break
    print()
    guess=input("guess a character")
    guesses+=guess

    if guess not in word:
        turns-=1
        print("wrong guess")
        print("you have",+ turns,"more guesses")
        if turns==0:
            print("you loose")

