import random #
def print_colored_text(text, color_name):                                         #create function that takes in text and color name
    colors = {                                                                    #color list dictionary with ansi code
        'black': '\033[30m',                                                      #black text color
        'red': '\033[31m',                                                        #red text color
        'green': '\033[32m',                                                      #green text color
        'yellow': '\033[33m',                                                     #yellow text color
        'blue': '\033[34m',                                                       #blue text color
        'magenta': '\033[35m',                                                    #magenta text color
        'cyan': '\033[36m',                                                       #cyan text color
        'white': '\033[37m',                                                      #white text color
        'reset': '\033[0m',                                                       #reset text color to default
    }
    
    color_code = colors.get(color_name.lower(), '\033[37m')                       #get the ansi color code for the given color default to white if no color found
    print(f"{color_code}{text}\033[0m")                                           #print the text with the given color followed by the reset code

name = input ("What is your name? ")                                              #ask what is your name                
print ("Hello" ,name)                                                             #print Hello (name)
print ("The game is to find the color of the text")                               #print The game is to find the color of the text
colors = ['black', 'red', 'green','yellow','blue','magenta', 'cyan', 'white']     #create a list if akk the colors above
correct = 0                                                                       #set correct to 0
rounds = 0                                                                        #set rounds to 0
while True:                                                                       #forever loop
    print_color = random.choice(colors)                                           #get random color from the color list
    text_color = random.choice (colors)                                           #gets text from the colors list
    print_colored_text(text_color, print_color)                                   #print the text in the color

    while True:                                                                   #forever loop
        color = input("Write the color: ")                                        #ask user to Write the color
        
        if color not in colors:                                                   #if the color is not in the color list
            print(f"Please enter one of the following colors: {', '.join(colors)}")#print Please enter one of the following colors:
        elif  color == print_color:                                               #otherwise if the user gueesses the random color
            print ("You got it!")                                                 #display you got it
            correct +=1                                                           #add one score to correct
            break                                                                 #end forever loop
        else:                                                                     #if the user gueeses wrong
            print ("Incorrect!")                                                  #print wrong
            break                                                                 #end forever loop
    
    rounds +=1                                                                    #add one to rounds
    
    while True:                                                                   #forever loop
        play_again = input(f"You have gotten {correct} out of {rounds}. Do you want to play again?")#ask the user if they want to play again
        
        if play_again == "no":                                                                      #if they say no
            print ("Bye!")                                                                          #end loop
            exit()                                                                                  #exit game
        if play_again == "yes":                                                                     #if they want to play again
            break                                                                                   #end loop
        else:                                                                                       #if something else said
            print ("Invalid Response")                                                              #display invalid response
        

    

    





