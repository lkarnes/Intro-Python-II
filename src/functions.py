import textwrap
wrapper = textwrap.TextWrapper(width=35) 

def searchroom(player):
    print('Items Found in room:')
    if len(player.room.items) > 0:
        for index,item in enumerate(player.room.items):
            print(str(index+1)+ ': ' + item.name)
    else: 
        print('The Room is Empty...')
    selection = input("""
_____________________________
|Controls:                  |
|Enter get {item name} to   |
|add to your inventory.     |
|                           |  
|Otherwise enter 0 to       |
|leave the search box       |
|___________________________|
Enter Input:""")
    selection = selection.split(' ')
    if(len(selection) == 2 and not selection == 0):
        if(selection[0] == 'take'):
            for item in player.room.items:
                found = False
                if(item.name.lower() == selection[1].lower()):
                    found = True
                    player.inventory.append(item)
                    player.room.items.remove(item)
                    item.__str__()
                    if item.value: 
                        action = input(f'Would you like to take the {item.name}? y/n: ')
                        if action == 'y':
                            player.gold += item.value
                            player.room.items.remove(item)
                        else:
                            print('item left behind')
                    moveon = input(f"click anything to continue: ")                
            if not found:
                print('##item was not found##')   



   

def openinventory(player):
    print("Items:")
    if(len(player.inventory) < 1):
        print("Inventory is empty...")
    else:
        for index,item in enumerate(player.inventory):
            print(f"{index+1}: {item.name}")
    action = input("""
_____________________________
|Controls:                  |
|Enter drop {item name} to  |
|remove it from your        |
|inventory.                 |
|                           |  
|Otherwise enter 0 to       |
|leave inventory            |
|___________________________|
Enter Input: """)
    action = action.split(' ')
    if(len(action) == 2 and not action == 0):
        if action[0] == 'drop':
            for item in player.inventory:
                if action[1] == item.name:
                    item.on_drop()
                    player.inventory.remove(item)
                    player.room.items.append(item)
                    moveon = input(f"click anything to continue: ")
        elif action == 0:
            print('returning to navigation')
        elif action[0] == 'enchant':
            print('...')
        else:  
            print("Please Try again with a valid input")
