from room import Room
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",[Item("Golden-Key", "A mysterious gold key from a unknown origin")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('Rusted-Long-Sword', 'An ancient sword found impaled into a body now made of only bones.')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[]),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Main
from player import Player
import textwrap
# Make a new player object that is currently in the 'outside' room.
player = Player('Logan', room['outside'], [["sword", "made from steel found in an ancient native burial ground"],["sword", "made from steel found in an ancient native burial ground"]])

#text wrapper and wraps
wrapper = textwrap.TextWrapper(width=35)  
location = wrapper.wrap(text=player.room.name)
description = wrapper.wrap(text=player.room.description)

#search rooms function

def searchroom(room):
    print('Items Found in room:')
    for index,item in enumerate(room.items):
        print(str(index+1)+ ': ' + item.name)
    selection = input("""
____________________________
|Controls:                 |
|Enter get {item name} to  |
|add to your inventory.    |
|                          |  
|Otherwise enter 0 to      |
|leave the search box      |
|__________________________|
Enter Input:""")
    selection = selection.split(' ')
    if(len(selection) == 2 and not selection == 0):
        if(selection[0] == 'take'):
            for item in room.items:
                if(item.name == selection[1]):
                    player.inventory.append(item)
                    descwrapper = wrapper.wrap(text=item.description)
                    print(len(descwrapper))
                    moveon = input(f"""
____________________________
Name: {item.name}

Description:
{descwrapper[0]}
{descwrapper[1]}
____________________________
click anything to continue:
""")
    else:
        print('please enter a valid action and item')
# Write a loop that:
selection = 0
while selection != 'q':
    print(f"\nLocation:")
    [print(line) for line in location]
    print(f"\nDescription:")
    [print(line) for line in description]
    selection = input("""
_____________________________
|Controls:                  |
|choose a direction: N E S W|
|Search Room: D             |
|Open Inventory: I          |
|___________________________|
Enter Input: """)
    selection = selection.lower()
    if selection == 'n':
        if(not hasattr(player.room, "n_to")):
            print('\n########\nyouve hit a dead end try another route\n########\n')
        else:
            player.room = player.room.n_to
    elif selection == 'e':
        
        if(not hasattr(player.room,"e_to")):
            print('youve hit a dead end try another route')
        else:
            player.room = player.room.e_to
    elif selection == 's':
        
        if(not hasattr(player.room,"s_to")):
            print('youve hit a dead end try another route')
        else: 
            player.room = player.room.s_to
    elif selection == 'w':
        
        if(not hasattr(player.room,"w_to")):
            print('youve hit a dead end try another route')
        else: 
            player.room = player.room.w_to
    elif selection == 'q':
        print("game over")  
    elif selection == 'd':
        searchroom(player.room)
    else: 
        print('PLEASE ENTER A VALID INPUT')
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
