inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i not in inventory:
            inventory.setdefault (str(i), 1)
        else:
            inventory[i] = inventory[i] + 1
    return inventory

inv = addToInventory(inv, dragonLoot)
print(inv)
