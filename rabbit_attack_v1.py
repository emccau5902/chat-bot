#  Copyright (c) 2016 Jon Cooper
#   
#  This file is part of rabbit-attack.
#  Documentation, related files, and licensing can be found at
# 
#      <https://github.com/joncoop/rabbit-attack>.

playing = True

while playing:

    num_knights = 5
    rabbit_is_alive = True

    print("Look, a cute little bunny rabbit.")

    while rabbit_is_alive and num_knights > 0:
        answer = input("Shall we use the Holy Hand Grenade? (y/n)")

        if answer == "y":
            use_grenade = True
        else:
            use_grenade = False

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
        
    answer = input("Would you like to play again? (y/n)")

    if answer == "y":
        playing = True
    else:
        playing = False

print("Goodbye. Thanks for playing!")
        
