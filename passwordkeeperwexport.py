'''
Author: Olivia Anikstein
4/2/23
Description: Find a safe place to keep your passwords!
Challenges: All
'''#Flower pot
import csv
import time
import os
import random

def add_entry(websites, usernames, passwords):
    '''
    Adds an entry to the parallel array of websites, usernames, and passwords
    Args:
        websites (list): the list of websites
        usernames (list): the list of usern ames
        passwords (list): the list of passwords
    Returns:
        parallel array: newly added to array of websites, usernames, and passwords
    '''
    website = input("Enter a website: ")
    username = input("Enter a username: ")
    password = input ("Enter a password (press 'g' to generate a random password): ")

    if password.lower() == "g":
        password = generate_password()
    websites.append(website)
    usernames.append(username)
    passwords.append(password)
def print_entry(website, username, password):
    '''
    Takes three elements and prints them neatly in an f-string
    Args:
        website (str)
        username (str)
        password (str)
    Returns: 
        prints: website name, the username, and the password
    '''
    print(f'''
website: {website}
username: {username}
password: {password}
''')
def get_index(websites):
    '''
    What is the index of the given website in website
    Args:
        websites (list): the list of websites
    Returns:
        int: index of the given website
    '''
    while True:
        website = input("Enter a website: ")

        if website in websites:
            return websites.index(website) #store the website index in the websites 
        else:
            print ("That is not a website")
def change_entry(websites, usernames, passwords):
    '''
    Allow the user to change usernames and passwords
    Args:
        websites (list): the list of websites
        usernames (list): the list of usern ames
        passwords (list): the list of passwords
    Returns: 
        updated entry
    '''
    index = get_index(websites)
    websites[index] = input('Enter new website: ')#Ask the user to enter a new website and store the website they input in the website index
    usernames[index] = input('Enter new username: ')
    passwords[index] = input('Enter new password: ')
def delete_entry(websites, usernames, passwords):
    '''
    Allow the user to delete an entry
    Args:
        websites (list): the list of websites
        usernames (list): the list of usern ames
        passwords (list): the list of passwords
    Returns:
        deletes entry
    '''
    index = get_index(websites)
    websites.pop(index)#removing the website inside the parentheses to the list thats given 
    usernames.pop(index)
    passwords.pop(index)
def export_entries(data, filename, header=None):
    '''
    Exports a list of lists to a CSV file.

    Args:
        data (list of lists): The data to be written to the CSV file.
        filename (str): The name of the CSV file to be created.
        header (list, optional): A list of strings representing the header row. 
                                 Defaults to None.
    '''
    
    with open(filename, 'w', newline='') as csvfile:            #open a new csv file to write to and open it as a csv file
        writer = csv.writer(csvfile)                            #start the writer to edit the file
        
        if header:                                              #if there is a header
            writer.writerow(header)                             #write the header row to the file
        
        writer.writerows(data)                                  #write all rows needed with given data

def enter_code(password, tries):
    '''
    Allow the user to enter a master password to enter the code
    Args:
        password (str): secret code to get in
        tries (int): number of times the user can try
    Returns:
        bool: True if login was successful
    '''
    for i in range(tries):
        check_password = input("Enter your secret code: ")

        if check_password == password:
            print ("Welcome")
            time.sleep(1)
            return True
        else:
            print ("incorrect")
    print('Access denied')
    time.sleep(1)
    return False
def get_password_length():
    '''
    Allow the user to decide how long they want the master password to be
    Args:
        None
    Returns: 
        int: length
    '''
    while True:
        try:#try/test
            length = int(input('Enter the desired password length: '))#ask the user to input their desired password length 
            return length
        except ValueError: #except if it is not a number
            print('Enter an integer')
def secure_password(password, length, display):
    '''
    Check how complex/secure passwords are
    Args:
        Passwords (string)
    Returns
        bool: True/False based on if password is secure
    '''
    if len(password) < length or password.lower() == password or password.upper() == password or not any(char.isdigit() for char in password) or not any(char in password for char in list('!@#$%^&*()_+')):
        if display:
            print(f"The password {password} is insecure")
        return False
    else:
        if display:
            print(f"The password {password} is secure")
        return True
def generate_password():
    '''
    Generates a random password
    Args:
        None
    Returns:
        str: generated password
    '''
    length = get_password_length()

    while True:
        pwd = ''.join(random.sample(list('abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345678910!@#$%^&*()_+'), length))

        if secure_password(pwd, length, False):
            return pwd
def main():
    websites = []
    usernames = []
    passwords = []

    secret_code = input('What do you want your secret password to be? ')
    time.sleep(1)
    os.system('cls')

    add_entry(websites, usernames, passwords)

    if not enter_code(secret_code, 3):
        exit()

    while True:
        option = input('''What do you want to do? (Enter 'q' to quit) 
1. Add an entry 
2. Print all passwords
3. Print a password 
4. Change an entry
5. Delete an entry
6. Export list of passwords to CSV file
7. Check the security of a password 
8. Generate a master password to enter the password keeper

        ''')
        
        if option.lower() == "q":
            break
        elif option == "1":
            add_entry(websites, usernames, passwords)
        elif option == "2":
            for index in range(len(websites)):
                print_entry(websites[index], usernames[index], passwords[index])
        elif option =="3":
            index = get_index(websites)
            print_entry(websites[index], usernames[index], passwords[index])    
        elif option == "4":
            change_entry(websites, usernames, passwords)
        elif option == "5":
            delete_entry(websites, usernames, passwords)
        elif option == "6":
            entries = []

            for i in range(len(websites)):
                entries.append([websites[i], usernames[i], passwords[i]])
            export_entries(entries, 'data.csv', ['Website', 'Username', 'Password'])
            print('Export successful! Your data is stored in data.csv')
        elif option == "7":
            pwd_access = input('Would you like to check a website password (w) or enter manually (m) ').lower()

            if pwd_access == 'w':
                password = passwords[get_index(websites)]
            else:
                password = input('Enter password: ')
            length = get_password_length()
            secure_password(password, length, True)
        elif option == "8":
            pwd = generate_password()
            print(f'Your generated password is {pwd}')
            change_pwd = input('Would you like to replace a password with this one? y/n ')

            if change_pwd.lower() == 'y':
                index = get_index(websites)
                passwords[index] = pwd
        else:
            print('invalid')
main()