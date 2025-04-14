rooms = { 
    'kitchen': {
        'description':'You are in the kitchen. There is a rusty knife here.',
        'north':'',
        'item':'',
    },
    'Living room': { 
         'description':'You are in the living room. A shadow looms...',
        'north':'Kitchen',
        'item':'Bedroom',
    },

    'Bedroom': {
        'description':'You are in a cozy bedroom. A treasure chest glows.',
        'West':'Living Room',
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

