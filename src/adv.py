from room import Room
from player import Player
from item import Item

# Declare all the rooms

spitoon = Item("Spitoon", "This is a bucket to spit in")
old_rag = Item("Old Rag", "This is a bucket to spit in")
compass = Item("compass", "This is a bucket to spit in")
spitoon = Item("Spitoon", "This is a bucket to spit in")
spitoon = Item("Spitoon", "This is a bucket to spit in")
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [spitoon, old_rag, compass]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [spitoon, old_rag]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [spitoon, old_rag]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [spitoon, old_rag]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [spitoon, old_rag]),

    'boomboom_room': Room("BoomBoom Room", """You've found the long-lost boom boom room! Get the chanpagin ready the ladies are on the way.Why would you want to leave. The only exit is to the south.""", [spitoon, old_rag]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['boomboom_room']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
current_player = Player("chuckD", room['outside'], None)
# spitoon = Item('spitoon', 'a bucket to spitoon')
# Write a loop that:
print(current_player.item)
valid_directions = ['n', 'e', 's', 'w']
valid_items = ['spitoon', 'oldrag', 'compass']
while True:
    # * Prints the current room name
    print(f'You are currently in {current_player.current_room.name}')
    # * Prints the current description (the textwrap module might be useful here).
    print(
        f'{current_player.current_room.description}, Items: {", ".join([item.name for item in current_player.current_room.item])}\n')

    # * Waits for user input and decides what to do.
    direction = input(f'Where would you like to go enter a direciton?\n  ')
    if direction in valid_directions:
        try:
            current_player.move(direction)
            print(f'{current_player.current_room.name}')
        except:
            print('YOU DIED!!!')
            break
    # If the user enters "q", quit the game.
    elif direction.lower() == 'q':
        print('Thanks for playing!')
        break

    elif direction.lower() == 'spitoon':
        print(current_player.pickup(spitoon))
    elif direction.lower() == 'drop spitoon':
        print(current_player.drop(spitoon))

    elif direction.lower() == 'oldrag':
        print(current_player.pickup(old_rag))
    elif direction.lower() == 'drop oldrag':
        print(current_player.drop(old_rag))

    elif direction.lower() == 'compass':
        print(current_player.pickup(compass))
    elif direction.lower() == 'drop compass':
        print(current_player.drop(compass))

    else:
        # Print an error message if the movement isn't allowed.
        print(f'Invalid Direction! {current_player.current_room.name}')
        direction = input(f'Where would you like to go? ')
#


#


#
