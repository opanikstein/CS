import time
import datetime
def print_colored_text(text, color_name):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m',  # Reset to default
    }
    
    color_code = colors.get(color_name.lower(), '\033[37m')  # Default to white if color not found
    print(f"{color_code}{text}\033[0m")  # Print text with color and reset
def input_colored_text(text, color_name):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m',  # Reset to default
    }
    
    color_code = colors.get(color_name.lower(), '\033[37m')  # Default to white if color not found
    return input(f"{color_code}{text}\033[0m")  # Print text with color and reset

print ("Alarm!")
current_time = datetime.datetime (2024, 10, 23, 6, 50, 0)
print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    snooze = input ("Snooze? yes/no: ")

    if snooze == "yes":
        print_colored_text ("Sleep for 5 more minutes", 'blue')
        time.sleep(5)
        print_colored_text ("Alarm!", 'cyan')
        current_time += datetime.timedelta(minutes=5)
        print(current_time.strftime("%H:%M:%S"), end='\r')
    elif snooze == "no":
        current_time += datetime.timedelta(minutes=5)
        break
    else:
        print_colored_text ("Invalid Response!", 'red')

print_colored_text ("Get up!", 'magenta')
print_colored_text ("Brush teeth and hair", 'magenta')
print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    makeup = str.lower (input ("Makeup? yes/no: "))
    if makeup == "yes":
        print ("Put makeup on", 'white')
        current_time += datetime.timedelta(minutes=5)
        break
    elif makeup == "no":
        print_colored_text ("Get dressed", 'yellow')
        break
        current_time += datetime.timedelta(minutes=10)
    else:
        print_colored_text ("Invalid Response!", 'red')
print(current_time.strftime("%H:%M:%S"), end='\r')
while True:
    sweatpants = str.lower (input ("Cold enough to wear sweatpants? yes/no: "))
    if sweatpants == "yes":
        print_colored_text ("Put sweatpants on", 'green')
        current_time += datetime.timedelta(minutes=5)
        break
    elif sweatpants == "no":
        print ("Put shorts on")
        break
        current_time += datetime.timedelta(minutes=3)
        print(current_time.strftime("%H:%M:%S"), end='\r')
    else:
        print ("Invalid Response!")
print(current_time.strftime("%H:%M:%S"), end='\r')
while True:
    too_hot_for_a_sweatshirt = str.lower (input ("Too hot for a sweatshirt? yes/no: "))
    if too_hot_for_a_sweatshirt == "yes":
        print_colored_text ("Put T-shirt on", 'cyan')
        current_time += datetime.timedelta(minutes=2)
        print(current_time.strftime("%H:%M:%S"), end='\r')
        break
    elif too_hot_for_a_sweatshirt == "no":
        print_colored_text ("Put sweatshirt on", 'magenta')
        current_time += datetime.timedelta(minutes=18)
        break
    else:
        print_colored_text ("Invalid Response!", 'red')
while True:
    pancakes_for_breakfast = str.lower (input ("Pancakes for breakfast? yes/no: "))
    if pancakes_for_breakfast == "yes":
        print_colored_text ("eat pancakes", 'yellow')
        print_colored_text ("leave for school", 'blue')
        current_time += datetime.timedelta(minutes=23)
        print(current_time.strftime("%H:%M:%S"), end='\r')
        break
    elif pancakes_for_breakfast == "no":
        print_colored_text ("eat bagel", 'yellow')
        current_time += datetime.timedelta(minutes=17)
        print(current_time.strftime("%H:%M:%S"), end='\r')
        print_colored_text ("leave for school", 'green')
        break
    else:
        print_colored_text ("Invalid Response!", 'red')
    
    

    

    
