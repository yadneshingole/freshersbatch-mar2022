player_inventory={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
player2={'badges':20,'guns':4,'Smokes':10,'Health_Pack':14,'missions':23}

def displayInventory(inventory):
    print("Inventory:")
    total_items=0
    for key,value in inventory.items():                 #Looping through the dictionary
        print(f'{value} {key}')                         
        total_items += value                            #Stores the total items 
    print("Total number of items: " + str(total_items))

displayInventory(player_inventory) #Calling a fucntion
displayInventory(player2)
