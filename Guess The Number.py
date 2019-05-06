import random
import simplegui
import math

secret_number =10 
high = 10
low = 0
count = 9
# helper function to start and restart the game
def new_game():
    global secret_number,count
    secret_number = random.randrange(low,high)
    if (high == 100):
        count = 7
    else:
        count = 10
    print" \nNew Game is starting !!!\n" 
   
    
def range100():
    print "\nRange is now 1-100:-"
    global high,count
    high=100
    new_game()

def range1000():
    print "\nRange is now 1-1000:-"
    global count,high
    high = 1000
    new_game()   
    
def input_guess(guess):
    global count
    count -= 1
    print "No of turns left",count
    print "Guess was ", int(guess)  
    GUESS = int(guess)
    if(count ==0 and GUESS != secret_number):
        print "You ran out of turns!!Correct Answer :",secret_number
        new_game()
    elif(GUESS == secret_number):
        print "Correct"
        new_game()
    elif(GUESS > secret_number):
        print "Lower"
    else:
        print "Higher"
    

frame = simplegui.create_frame("Guess the Number",300,300)
button1 = frame.add_button("1-100",range100,200)
button2 = frame.add_button("1-1000",range1000,200)
guessed = frame.add_input("Enter guess:",input_guess,200)

frame.start()

#new_game()


