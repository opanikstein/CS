#cat
import random                                                                                
while True:
    game = input ("Rock, Paper, Scissors or Pick a color in the Rainbow: ").lower()         #choose either Rock Paper Scissors game or Pick a color in the rainbow game
    if game == "volleyball":                                                                #passord is volleyball
        user_guess = input("Rock, Paper, Stick, or Scissors: ").lower()                     #display "Rock Paper Scissors or Stick" for the user to choose

        if user_guess == "rock":                                                            #if the user guesses rock
                print ("The computer guessed scissors. You win!")                           #display "The computer guessed scissors. You win!"
        elif user_guess == "paper":                                                         #if the user gueses paper
                print ("The computer guessed rock. You win!")                               #display "The computer guessed rock. You win!"
        elif user_guess == "scissors":                                                      #if the user guessed scissors
                print ("The computer guessed paper. You win!")                              #display "The computer guessed paper. You win!"
    elif game == "rock, paper, scissors":                                                   #if the user chooses to play Rock Paper Scissors                                 
        score = 0                                                                           #set the score to zero
        options = ["rock", "scissors", "paper","stick"]                                     #weapon options are rock, paper, scissors, and stick
        score_limit = 3                                                                     #the score limit is 3


        while score <score_limit:                                                           #when the score is less than the score limit                                                          
            user_guess = input("Rock, Paper, Stick, or Scissors: ").lower()                 #display "Rock Paper Scissors or Stick" for the user to choose
            computer_guess = random.choice(options)                                         #computer randomly chooses an option
            print (f"The user chose {user_guess}, while the bot chose {computer_guess}")    #display "The user chose {user_guess}, while the bot chose {computer_guess}"
            if user_guess == "quit":                                                        #if the user chooses quit
                print ("Bye!")                                                              #display "Bye!"
                break                                                                       #end loop
            elif user_guess == computer_guess:                                              #if the user guess and the computer guess are the same
                print ("Tie! Try again")                                                    #display "Tie! Try again"
            elif user_guess == "scissors" and computer_guess == "paper":                    #if the user guesses scissors and the computer guesses paper
                print ("You win!")                                                          #print "You win!"
                score +=1                                                                   #add 1 to score
            elif user_guess == "scissors" and computer_guess == "rock":                     #if the user guess is scissors and the computer guess is rock
                print ("You lose!")                                                         #display "You lose!"
                score -=1                                                                   #subtract 1 from score
            elif user_guess == "paper" and computer_guess ==  "rock":                       #if the user guesses paper and the computer guesses rock
                print ("You win!")                                                          #print "You win"
                score +=1                                                                   #add 1 to score
            elif user_guess == "paper" and computer_guess == "scissors":                    #if the user guesses paper and the computer guesses rock
                print ("You lose")                                                          #display "You lose"
                score -=1                                                                   #subtract 1 from score
            elif user_guess == "rock" and computer_guess == "paper":                        #if the user guesses rock and the computer guesses paper
                print ("You lose")                                                          #display "You lose"
                score -=1                                                                   #subtract 1 from score
            elif user_guess == "stick" and computer_guess == "rock":                        #if the usre guesses stick and the computer guesses rock
                print ("You lose")                                                          #display "You lose"
                score -=1                                                                   #subtract one from score
            elif user_guess == "stick" and computer_guess == "paper":                       #if the user guesses stick and the computer guesses paper
                print ("You win!")                                                          #display "You win!"
                score +=1                                                                   #add 1 score
            elif user_guess == "stick" and computer_guess == "scissors":                    #if the user guesses stick and the computer guesses scissors
                print ("You lose")                                                          #display "You lose"        
                score -=1                                                                   #subtract 1 from score
            elif user_guess == "rock" and computer_guess == "scissors":                     #if the computer guesses rock and the computer guesses scissors
                print ("You win!")                                                          #print "You win!"                                                        
                score +=1                                                                   #add 1 to score
            else:                                                                           #if user puts in something else
                print ("Invalid Respones!")                                                 #dsplay "Invalid Respones!"
            print(score)                                                                    #display score anytime score is said in code



    elif game == "pick a color in the rainbow":                                             #the second game is pick a color in the rainbow
        score = 0                                                                           #set score to 0
        colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]             #color options are red, orange, yellow, green, blue, purple, pink
        score_limit =3                                                                      #set the score limit to 3

        while score <score_limit:                                                           #when the score is less than the score limit 
            user_guess = input ("Pick a color in the rainbow: ").lower()                    #user chooses a color in the rainbow
            computer_guess = random.choice(colors)                                          #computer randomly chooses a color
            print (f"The user chose {user_guess}, while the bot chose {computer_guess}")    #display "The user chose {user_guess}, while the bot chose {computer_guess}"
            if user_guess == "quit":                                                        #if the user chooses to quit
                print ("Bye!")                                                              #display "Bye!"
            if user_guess == computer_guess:                                                #if the user guess is  equal to the computer guess
                print ("You win!")                                                          #display "You win!"
                score +=1                                                                   #add 1 to score
            if user_guess!= computer_guess:                                                 #if the user guess is not equal to the computer guess
                print ("You lose!")                                                         #display "You lose!"
                score -=1                                                                   #subtract 1 from score
            else:                                                                           #if user puts in something else
                print ("Invalid Response")                                                  #dsplay "Invalid Respones!"
            print (score)                                                                   #display score anytime score is said in code
                                                                                            #display picture
print (''')  (                                                                              
     (   ) )
      ) ( (
 mrf_______)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'
    ''')



