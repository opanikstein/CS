def add_entry(websites, usernames, passwords):
    '''
    Adds an entry to the parallel array of websites, usernames, and passwords
    Args:
        websites (list): the list of websites
        usernames (list): the list of usernames
        passwords (list): the list of passwords
    Returns:
        parallel array: newly added to array of websites, usernames, and passwords
    '''
    website = input("Enter a website: ")
    username = input("Enter a username: ")
    password = input ("Enter a password:")
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
            return websites.index(website)
        else:
            print ("That is not a website")
def change_entry(websites, usernames, passwords):
    index = get_index(websites)
    websites[index] = input('Enter new website: ')
    usernames[index] = input('Enter new username: ')
    passwords[index] = input('Enter new password: ')
def main():
    websites = []
    usernames = []
    passwords = []

    add_entry(websites, usernames, passwords)

    while True:
        option = input("What do you want to do? (Enter 'q' to quit) 1. Add an entry 2. Print all passwords 3. Print a password 4. Change an entry ")
        
        if option.lower() == "q":
            break
        if option == "1":
            add_entry(websites, usernames, passwords)
        elif option == "2":
            for index in range(len(websites)):
                print_entry(websites[index], usernames[index], passwords[index])
        elif option =="3":
            index = get_index(websites)
            print_entry(websites[index], usernames[index], passwords[index])    
        elif option == "4":
            change_entry(websites, usernames, passwords)
main()