'''
Author: Olivia Anikstein
4/2/23
Description: Order food or play a game. Have fun!!
Challenges: All
'''#Flower pot


import random 
mains = ["chicken parmesan", "penne alla vodka", "steak frites", "salmon", "lasagna" "ravioli", "caesar salad", "margherita pizza", "sandwich"]
main_prices = [23,18, 28, 26, 18, 18, 16, 17, 20]
drinks = ["water", "sprite", "diet coke", "coke", "mojito", "coffee", "sparkling water", "mint water", "shirley temple"]
drink_prices = [0, 4, 4, 4, 7, 6, 2, 2, 6]

while True:
    game = input("Would you rather order food or play rock paper scissors?")

    if game == 'order food':
        try:#ask
            num_of_items = int(input("How many items would you like"))#ask user how many items they would like to get

            if num_of_items < 1 or num_of_items > 20:#if number of items is more than 1 and less than 20
                print('Please enter a number between 1 and 20')#tell user to enter a number between 1 and 20
                continue #go back to start of loop
        except ValueError: #if something that is not an integer entered
            print('Enter an integer please')#display "Enter an integer please"
            continue#go back to start of loop
        
        total_price = 0#the total price of the items is 0
        used = []#list of items that have been used
        
        for i in range(num_of_items):#repeats for the number of items the user entered
            main = random.choice(mains)#choose a random main 
            drink = random.choice(drinks)#choose a random drink

            if main+drink in used:#if the main and drink combo is already used 
                continue#go back
            used.append(main+drink)#add main and drink to the list
            main_price = main_prices[mains.index(main)]#finding the index of main in mains and using that index to find the corresponding price
            drink_price = drink_prices[drinks.index(drink)]#finding the index of drink in drinks and using that index to find the corresponing price
            print(f'{main} with {drink}, Your cost is ${main_price} + ${drink_price} = ${main_price+drink_price}')#display the total price of the main and drinks 

            total_price += main_price + drink_price #the total price is equal to the main and drink price combined
            
        print (f'${total_price}')#display the total price

    if game == "rock paper scissors":                                                                #passord is rock paper scissors
        user_guess = input("Rock, Paper, or Scissors: ").lower()                     #display "Rock Paper or Scissors" for the user to choose

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



    
        

