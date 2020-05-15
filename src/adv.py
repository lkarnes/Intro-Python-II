from room import Room
from item import Item, Loot, Weapon
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",[Item("Golden-Key", "A mysterious gold key from a unknown origin")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('Rusted-Long-Sword', 'An ancient sword found impaled into a body now made of only bones.')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[Loot('Gold-Coin', 'A glistening gold coin, this may mean you are getting closer to the treasure that hides ahead...',5)],),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[Item('Broken-Shovel', 'Its a Broken shovel...')]),

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
from functions import searchroom, openinventory
# Make a new player object that is currently in the 'outside' room.
player = Player('Logan', room['outside'], [["sword", "made from steel found in an ancient native burial ground"]], 0)

#text wrapper and wraps
wrapper = textwrap.TextWrapper(width=35)  
        
charecters = {
    'n':'n_to',
    'e':'e_to',
    's':'s_to',
    'w': 'w_to',
    'q': 'q',
    'd': 'd',
    'i': 'i',
    'c':'c'
}
key_list = list(charecters.keys())
# Write a loop that:
selection = 0
print('''
_____________________________
|Controls:                  |
|choose a direction: N E S W|
|Search Room: D             |
|Open Inventory: I          |
|Controls: C                |
|___________________________|
      ''')
while selection != 'q':
    location = wrapper.wrap(text=player.room.name)
    description = wrapper.wrap(text=player.room.description)
    print(f"\n__________________________\nLocation:")
    [print(line) for line in location]
    print(f"\nDescription:")
    [print(line) for line in description]
    selection = input("""\nEnter Input: """)
    selection = selection.lower()
    while selection not in key_list:
        selection = input('not a valid command enter a new value: ')
    try:
        if selection == 'd':
            searchroom(player)
            print('left searchbox')
        elif selection == 'q':
            print("game over")  
        elif selection == 'i':
            openinventory(player)
            print('left searchbox')
        elif selection == 'c':
            print("""
_____________________________
|Controls:                  |
|choose a direction: N E S W|
|Search Room: D             |
|Open Inventory: I          |
|Controls: C                |
|___________________________|
""")
            input('enter anything to continue: ')
        else:
            player.room = getattr(player.room, f'{selection}_to')
            print(player.room.name)
    except:
        print('youve hit a dead end try another route')
