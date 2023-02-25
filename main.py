import sys
import random as rand
import time


def game_start():
    print("+-----------------------------+")
    print("|        8 ball game          |")
    print("+-----------------------------+")
    print("|1.ask any yes or no question |")
    print("|2.type quit to quit...       |")
    print("-------------------------------")


def game_loop():
    user_input = input("question: ")
    if user_input == "quit":
        sys.exit("fuck this shit i am out")
    else:
        fate = rand.randint(0, 16)
        fate = fate // 4
        match fate:
            case 0:
                print("yes")
            case 1:
                print("no")
            case 3:
                time.sleep(2)
                print("maybe")
            case 4:
                sys.exit("...your asking to much")


game_start()
while True:
    game_loop()
