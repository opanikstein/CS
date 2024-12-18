import random

responses = ["Yes, of course", "No, definitely not", "Maybe, it is possible", "Ask again later"]
question_words = ["Is", "What", "Which", "When", "Where", "Who", "Why", "How", "Am"]
while True:
    question = input ("Ask the Magic 8 Ball a question: ")
    first_word = question.split()[0]
    
    if "?" in question or first_word.capitalize() in question_words:
        answer = random.choice(responses)
        print ("Magic 8 Ball Says: " + answer)
    else:
        print ("Invalid Response!")
        

    
    

