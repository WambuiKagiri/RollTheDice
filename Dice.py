import random
min = 1
max = 6

roll_again = "yes"

if roll_again == "yes":
    print "Rolling the dice.."
    print "The values are.."
    print random.randint(min, max)
    print random.randint(min, max)

else:
    exit(0)
roll_again = raw_input("Roll the dice again?")
