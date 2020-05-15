# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item
from room import Room
class Player: 
    def __init__(self, name, room, inventory, gold):
        self.name = name
        self.room = room
        self.inventory = []
        for item in inventory:
            item = Item(item[0], item[1])
            self.inventory.append(item)
        self.gold = 0