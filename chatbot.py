# PyChat 2K17

import random

def start():
    print(" _____ _                    _                         _              ")
    print("/__   \ |__  _ __ ___   ___| | ___ __ ___   ___  _ __| |_ ___  _ __  ")
    print("  / /\/ '_ \| '__/ _ \ / __| |/ / '_ ` _ \ / _ \| '__| __/ _ \| '_ \ ")
    print(" / /  | | | | | | (_) | (__|   <| | | | | | (_) | |  | || (_) | | | |")
    print(" \/   |_| |_|_|  \___/ \___|_|\_\_| |_| |_|\___/|_|   \__\___/|_| |_|")
    print("                                                                     ")

def end():
    print("______            ")
    print("| ___ \           ")
    print("| |_/ /_   _  ___ ")
    print("| ___ \ | | |/ _ \\")
    print("| |_/ / |_| |  __/")
    print("\____/ \__, |\___|")
    print("        __/ |     ")
    print("       |___/      ")

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup"]:
            return True
        elif answer in ["n", "no", "nope"]:
            return False
   
def has_keyword(statement, keywords):
    for word in keywords:
        if word == statement:
            return True

    return False

def get_random_response():
    responses = ["Uh, huh.",
                 "Oh, that's interesting",
                 "Do you really think so?",
                 "I'll bet.",
                 "Hmm.",
                 "Yeah?"]

    return random.choice(responses)

def get_response(statement):
    statement = statement.lower()
    if len(statement) == 0:
        response = "Could you repeat that?"
        return response
    
    family_words = ["mother", "father", "brother", "sister"]
    teacher_words = ["cooper", "school", "jl mann"]
    programmer_words = ["fuck"]
    
    if has_keyword(statement, family_words):
        response = "Tell me more about your family."
    elif has_keyword(statement, teacher_words):
        response = "I hear Mr. Cooper's class is really fun."
    elif has_keyword(statement, programmer_words):
        response = "Watch your mouth."
    else:
        response = get_random_response()

    return response

def naming():
    name = input("What is your name?")
    if name.isupper():
        name = input("Hey, try not yelling at me. Now, let's try that again, what is your name?")
    name = name.lower()
    if name == "throckmorton":
        name = input('Nice try, genius, what is your real name?')
    else:
        print("Say something to me, " + name + "!")
        return name

def play():
    talking = True
    print("Hello. I'm Throckmorton.")
    player_name = naming()

    while talking:
        statement = input(player_name + ":")
        
        if statement == "Goodbye":
            talking = False
        else:
            response = get_response(statement)
            print(response)

    print("Goodbye. It was nice talking to you.")

start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to chat again?")

end()
