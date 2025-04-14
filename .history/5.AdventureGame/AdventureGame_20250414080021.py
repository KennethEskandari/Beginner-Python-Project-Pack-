rooms = { 
    'kitchen': {
        'description':'You are in the kitchen. There is a rusty knife here.',
        'north':'',
        'item':'',
    },
    'Living room': { 
         'description':'You are in the living room. A shadow looms...',
        'south':'Kitchen',
        'east':'Bedroom',
    },

    'Bedroom': {
        'description':'You are in a cozy bedroom. A treasure chest glows.',
        'west':'Living Room',
        'item':'Treasure',
    },
}

current_room = 'kitchen'
inventory = []

while True: 
    print(rooms[current_room]['description'])

    if 'item' in rooms[current_room]:
        item = rooms[current_room]['item']
        print(f'You See An: {item}.')

    command = input('What do you want to do? >').lower()

    if command in ['north','east','south','west']:
        if command in rooms[current_room]:
            current_room = rooms[current_room][command]
        else: 
            print("You can't go that way.")

    elif command == 'get':
        if 'item' in rooms[current_room]:
            inventory.append(rooms[current_room]['item'])
            print(f'You Picked Up {rooms[current_room]['item']}.')
        else:
            print('There is nothing to pick up')
    elif command == 'inventory':
        print(f'Inventory: {inventory}')
    elif command == 'Quit':
        print("Thank you for playing")
        break
    else : 
        print("Invalid Command")
    
        