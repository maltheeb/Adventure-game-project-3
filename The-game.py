import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)
# print and sleep 2 sec


def intro():
    name = input("What is your name?\n")
    # save the random choice to use it later
    print_pause("You have arrived at your friend Mohammed's house")
    print_pause("You knock on the door")
    print_pause("Your friend asked who is there?")
    print_pause("So you answered him I'm " + name)
    print_pause("Mohammed: Hello, "+name+", welcome to my home")
    print_pause("Come with me")
# introduction


def choice_drink(rooms, meals, choice_room, counter):
    meals[1] = input("What do you want to drink?:\n"
                     "Water\n"
                     "Soda\n"
                     "Coffee\n").lower()
    print_pause("After a few seconds ..")
    if "water" == meals[1]:
        print_pause("This is your water!")
    elif "coffee" == meals[1]:
        print_pause("This is your coffee!")
    elif "soda" == meals[1]:
        print_pause("This is your soda!")
    else:
        print_pause("Sorry, but I don’t have it")
        choice_drink(rooms, meals, choice_room, counter)
# ask you about your drink and save it in meals[1]


def choice_dish(rooms, meals, choice_room, counter):
    meals[0] = input("What do you prefer:\n"
                     "Pie\n"
                     "Sandwich?\n").lower()
    print_pause("After a few seconds, ")
    if "pie" == meals[0]:
        print_pause("This is your Pie")
    elif "sandwich" == meals[0]:
        print_pause("This is your Sandwich")
    else:
        print_pause("Sorry, but I didn't prepare this meal")
        choice_dish(rooms, meals, choice_room, counter)
# ask you about you meal then save it in meals[0]


def lights():
    light = input("Do you prefer the light:\n"
                  "off\n"
                  "on\n").lower()
    if "on" == light:
        print_pause("Ok, I will keep it")
    elif "off" == light:
        print_pause("Ok, I turn it off")
    else:
        lights()
# ask you if you want a lights off or on


def living_room(rooms, meals, choice_room, counter):
    print_pause("You are in the living room")
    print_pause("Please sit down")
    choice_drink(rooms, meals, choice_room, counter)
    change_room(rooms, meals, choice_room, counter)
# You will stay in the livig room then go to the Kitchen


def kitchen(rooms, meals, choice_room, counter):
    print_pause("You are in the Kitchen")
    print_pause("Welcome, I prepared delicious meals for you")
    choice_dish(rooms, meals, choice_room, counter)
    choice_drink(rooms, meals, choice_room, counter)
    change_room(rooms, meals, choice_room, counter)
# take a meal then go to the bedroom


def stairs(rooms, meals, choice_room, counter):
    print_pause("Let's go upstairs")
    print_pause("I know that you are tired after traveling")
    print_pause("I have prepared the bedroom for you to take a rest")
    print_pause("This is the bedroom")
    lights()
    change_room(rooms, meals, choice_room, counter)
# You will go to bedroom then to the living room


def rotation(rooms, meals, choice_room, counter):
    if choice_room == "living_room":
        living_room(rooms, meals, choice_room, counter)
    elif choice_room == "stairs":
        stairs(rooms, meals, choice_room, counter)
    elif choice_room == "kitchen":
        kitchen(rooms, meals, choice_room, counter)
# take you to the first room in your visit


def change_room(rooms, meals, choice_room, counter):
    counter += 1
    if choice_room == "living_room" and counter < 3:
        choice_room = "kitchen"
        kitchen(rooms, meals, choice_room, counter)
    elif choice_room == "stairs" and counter < 3:
        choice_room = "living_room"
        living_room(rooms, meals, choice_room, counter)
    elif choice_room == "kitchen" and counter < 3:
        choice_room = "stairs"
        stairs(rooms, meals, choice_room, counter)
    else:
        stay = input("Do you want to stay at home?:\n"
                     "Yes\n"
                     "No\n").lower()

        if "yes" == stay:
            counter = 0
            rotation(rooms, meals, choice_room, counter)
        elif "no" == stay:
            print_pause("Ok, good bye!")
        else:
            change_room(rooms, meals, choice_room, counter)
# change your room


def visit_friend():
    rooms = ["living_room", "stairs", "kitchen"]
    meals = ["", ""]
    choice_room = random.choice(rooms)
    counter = 0
    intro()
    rotation(rooms, meals, choice_room, counter)


visit_friend()
