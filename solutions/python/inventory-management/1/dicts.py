"""Functions to keep track and alter inventory."""


def create_inventory(items):
    inventory = {}
    for item in items:
        inventory[item] = inventory.get(item,0)+1

    return inventory
    pass

def add_items(inventory, items):
    for item in items:
        
        inventory[item] = inventory.get(item, 0) + 1
    
    return inventory
    pass
    
def decrement_items(inventory, items):
    for item in items:
       
        if inventory.get(item, 0) > 0:
            inventory[item] -= 1
    return inventory
    pass



def remove_item(inventory, item):
    
    if item in inventory:
        del inventory[item]
    
    return inventory
    pass

def list_inventory(inventory):
    return sorted([(item, qty) for item, qty in inventory.items() if qty > 0])

    pass

