import random#bring in random

def chorus(name, home):#function is chorus and you enter your name and town you live in
    '''
    Prints the chorus of a song
    Args:
        None
    Returns:
        print: chorus
    '''
    print (f"The wheels on {name}'s bus go 'round and 'round!")#lyrics of first part of the chorus
    print (f"'Round and 'round, 'round and 'round")#lyrics of second part of the chorus
    print (f"The wheels on the bus go 'round and 'round")#lyrics of third part of the chorus
    print (f"All through {home}")#lyrics of fourth part of the chorus
def song():
    '''
    Prints an entire song using the chorus function
    Args:
        None
    Returns:
        print: Entire song
    '''
    chorus("Olivia", "Greenwich")#olivia is printed in the first time name is mentioned, and greenwich is mentioned the first time home is mentioned
    chorus("Melissa", "Larchmont")#melissa is printed in the second time name is mentioned, and larchmont is mentioned the second time home is mentioned
    print ("The doors on the bus go open and shut Open and shut, open and shut The doors on the bus go open and shut All through the town")#part of the normal verse
    print ("The wipers on the bus go swish, swish, swish Swish, swish, swish, swish, swish, swish The wipers on the bus go swish, swish, swish All through the town")#part of the normal verse
    print ("The signals on the bus go blink, blink, blink Blink, blink, blink, blink, blink, blink The signals on the bus go blink, blink, blink All through the town")#part of the normal verse
    print ("The horn on the bus goes beep, beep, beep, beep, beep, beep, beep, beep horn on the bus goes beep, beep, beep through the town")#part of the normal verse
    print ("The motor on the bus goes vroom, vroom, vroom, vroom, vroom, vroom, vroom, vroom, vroom The motor on the bus goes vroom, vroom, vroom All through the town")#part of the normal verse
    print ("The people on the bus go up and down and down, up and down people on the bus go up and down through the town")#part of the normal verse
    print ("The babies on the bus go, Wah, wah, wah, wah, wah, wah, wah, wah, wah The babies on the bus go, Wah, wah, wah All through the town")#part of the normal verse
    print ("The mommies on the bus go, Shh, shh, shh Shh, shh, shh, shh, shh, shh The mommies on the bus go, Shh, shh, shh All through the town")#part of the normal verse
    print ("The daddies on the bus go, I love you I love you, I love you The daddies on the bus go, I love you All through the town")#part of the normal verse
    chorus("Olivia", "Greenwich")#olivia is printed in the first time name is mentioned, and greenwich is mentioned the first time home is mentioned
    chorus("Melissa", "Larchmont")#melissa is printed in the second time name is mentioned, and larchmont is mentioned the second time home is mentioned
def add(a, b): #function is called add two numbers are entered to be added up
    '''
    Takes two numbers and adds them together
    Args:
        a (int): first number
        b (int): second number
    Returns:
        print: sum of a and b
    '''
    print (a+b)#display the two numbers added up
def print_list (array):#function is called print_list
    '''
    Takes a list and prints every element in that list individually (vertically)
    Args:
        array (list): given list
    Returns:
        print: every element in the given list vertically
    '''
    for item in array:#for loop
        print(item)#print the item
def in_list(array, element):#function called in_list
    '''
    Takes a list and element and returns a boolean based on if the element is in the list
    Args:
        array (list): given list
        element (any): element to be checked
    Returns:
        bool: True/False based on if element is in array
    '''
    return element in array#save element in the array
def get_integer(order):#funtion is called get_integer
    '''
    Asks the user for two numbers, uses is_integer to check input, returns the two integers
    Args:
        order (str): what kind of number (first, second, third...)
    Returns:
        int: number from user input
    '''
    while True: #while true loop
        try:#try/test
            number = int(input(f"Enter the {order} number: "))#input a number
            return number#save the number
        except ValueError:#except if it is not a number
            print('Not a number')#display not a number
def get_random():#function called get random
    '''
    Uses get_integers and prints a random number between the two given integers
    Args:
        None
    Returns:
        print: random number between a and b
    '''
    a = get_integer('first')#a is the first integer
    b = get_integer('second')#b is the second integer
    print (random.randint(a, b))#print a random integer in between a and b
def count_vowels(string):#count vowels is the string name
    '''
    Takes a string and returns the number of vowels in it 
    Args:
        string (str): string to count
    Returns:
        int: number of vowels
    '''
    count = 0#there are 0 vowels

    for char in string:#for loop (for characters in a string)
        if char in ['a', 'e', 'i', 'o', 'u']:#if the characters in the string have any vowels in them
            count += 1#add one vowel to the count
    return count#save the count
def reverse_string(string):#function called reverse string
    '''
    Takes a string and reverses it 
    Args:
        takes the users words and prints the reverse
    Returns:
        str: string reversed
    '''
    return string[::-1]#save string
def is_palindrome(string):#function is called is_palindrome
    '''
    Takes the users words and sees if it is a palindrome
    Args:
        string (str): word or phrase
    Returns:
        str: string reversed
    '''
    return string == reverse_string(string)#save string if it is equal to reverse_string
def get_initials(name):#get initials is function name
    '''
    Takes the users full name and prints the first letter of each words, their initials
    Args:
        fullname (str): fullname (first, middle, last)
    Returns:
        str: the first letter of each name
    '''
    names = name.split()#name is equal to the name and then split
    initials + ''#initials are printed in 

    for n in names:#for loop
        initials += n[0].upper() + ". "#initials 
        return initials#save initials
def replace_character(string, old, new):#function called replace character
    '''
    Takes a string, an old character, and a new character, and replaces every instance in the string of the old character with the new (without using string methods)
    Args:
        string (str): Word that is to be replaced
        old_character (str): The letter getting replaced
        new_character (str): The letter now going into the word
    Returns:
        str: the replacement, new word (if the word has (old_letter), replaces it with (new_letter))
    '''
    new_string = ''#new string is the initials

    for char in string:#for each character in the string
        if char == old: #ifthe character is old
            new_string += new #new string is added to new
        else:#if something else
            new_string += char#new string is added to the character
    return new_string#save string

def main():#main function (where you call the functions)
    while True:#while True loop
        option = input('Enter a number between 1 and 9: ')#input a number between 1 and 9

        if option == '1':#if it is option 1
            a = get_integer('first')#a is the first integer
            b = get_integer('second')#b is the second integer
            add (a, b)#add a and b
        elif option == '2':#if it is option 2
            song()#song is the function
        elif option == '3':#if option 3
            user_list = input('Enter a list of items (use spaces to separate each item) ').split(' ')#enter a list of itmes
            print_list(user_list)#print the list that the user made
        elif option == '4':#if it is option 4
            user_list = input('Enter a list of items (use spaces to separate each item) ').split(' ')#input a list of items
            check = input('Enter thing to check ')#enter a thing to check
            print(in_list(user_list, check))#print the list the user made and check to make sure it is true or fals
        elif option == '5':#if it is option 5
            get_random()#get random
        elif option == '6':#if it is option 6
            word = input('Enter a word or phrase: ')#have the user input a word or phrase
            print(count_vowels(word))#print the number of vowels in the word
        elif option == '7':#if it is option 7
            word = input('Enter a word or phrase: ')#have the user input a word or phrase
            print (reverse_string(word))#print the string in reverse
        elif option == '8':#if it is option 8
            word = input('Enter a word or phrase: ')#have the user input a word or phrase
            print (is_palindrome(word))#print whether or not the word is a palindrome
        elif option == '9':#if it is option 9
            text = input("Enter a word or phrase ")#have the user input a word or phrase
            old_character = input("Enter a letter to replace: ")#enter a letter to replace one of the letters
            new_character = input("Enter a letter that replaces the old character: ")#enter a letter that replaces the old character
            print(replace_character(text, old_character, new_character))#print the word or phrase with the replaced characters
main()#main
