import textwrap
wrapper = textwrap.TextWrapper(width=35) 
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def on_take(self):
        print(f'You picked up {self.name}')
        
    def on_drop(self):
        print(f'You dropped {self.name}')
        
class Weapon(Item):
    def __init__(self, name, description, damage, durability):
        super().__init__(name,description)
        self.damage = damage
        self.durabillity = durability
        self.enchanted = false
        
    def enchant(self):
        self.damage += 5
        
class Loot(Item):
    def __init__(self, name, description, value):
        super().__init__(name,description)
        self.value = value
        
    def __str__(self):
        descwrapper = wrapper.wrap(text=self.description)
        desc='\n'.join(map(str, descwrapper))
        print(f"""
__________________________________
{self.name}                
                           
Value: {self.value}        
----------------------------------
Description:               
{desc}                     
__________________________________
              """ )