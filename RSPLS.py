import random
def name_to_number(name):
    if(name == "rock"):
        return 0	
    elif(name== "Spock"):
        return 1
    elif(name== "paper"):
        return 2
    elif(name== "lizard"):
        return 3
    elif(name== "scissors"):
        return 4
    else:
        print("Wrong call!!Input doesn't exist:(")

def number_to_name(number):
    if(number == 0):
        return "rock";
    elif(number== 1):
        return "Spock"
    elif(number == 2):
        return "paper"
    elif(number== 3):
        return "lizard"
    elif(number == 4):
        return "scissors"
    else:
        print("Wrong call!!Input doesn't exist:(")
    

def rpsls(player_choice): 
    print "\n" 
    print("Player chooses %s " %(player_choice))
    
    number = name_to_number(player_choice)
    rand_number = random.randrange(0,5)
    name_computer = number_to_name(rand_number) 
    print("Computer chooses %s" %(name_computer))
    
    #if a tie occurs
    if(number == rand_number):
        print "Player and Computer tie"
    
    #checking who is the winner
    difference = number - rand_number
    if( (difference % 5)==3 or (difference%5)==4 ):
        print("Computer wins!")
    elif( (difference % 5)==1 or (difference%5)==2 ):
        print("Player wins!")
    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




