#  Copyright (c) 2016 Jon Cooper
#   
#  This file is part of rabbit-attack.
#  Documentation, related files, and licensing can be found at
# 
#      <https://github.com/joncoop/rabbit-attack>.

def confirm(question):
    answer = input(question + " (y/n)")

    if answer == "y":
        return True
    else:
        return False


playing = True

while playing:

    num_knights = 5
    rabbit_is_alive = True

    print("Look, a cute little bunny rabbit.")

    while rabbit_is_alive and num_knights > 0:
        use_grenade = confirm("Shall we use the Holy Hand Grenade?")

        if use_grenade:
            print("1... 2... 5... No, 3!")
            print("Boom!")
            rabbit_is_alive = False
        else:
            num_knights -= 1
            print("Oh, no! The rabbit just killed one of the knights!")
            print("Only " + str(num_knights) + " remain.")
        
    if num_knights > 0:
        print("The killer rabbit has been defeated. You win!")
    else:
        print("All of the knights are dead. You lose.")
        
    playing = confirm("Would you like to play again?")


print("Goodbye. Thanks for playing!")
        
