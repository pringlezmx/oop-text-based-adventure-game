from room import Room
from character import Enemy
from rpginfo import RPGInfo


spooky_castle = RPGInfo("the spooky castle")
spooky_castle.welcome()
RPGInfo.info()
RPGInfo.author = "AK"


kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining hall")

print("There are " + str(Room.number_of_rooms) + " rooms to explore.")

kitchen.set_description("a cooking place")
dining_hall.set_description("place to eat")
ballroom.set_description("place to dance")
#dining_hall.get_details()

kitchen.get_description()

#kitchen.describe()

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "zombie")
dave.set_conversation("hi i am dave")
dave.set_weakness("cheese")
dining_hall.set_character(dave)


currentroom = kitchen

while True:
    print("\n")
    
    inhabitant = currentroom.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        dave.talk()
        print("what will you fight with?")
        fight_with = input()
        outcome = dave.fight(fight_with)
        if outcome is False:
            print("you died")
            break
        else:
            print("you won")
            
    currentroom.get_details()
    command = input("> ")
    currentroom = currentroom.move(command)
    


RPGInfo.credit()