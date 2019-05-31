# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room, item):
        self.name = name
        self.current_room = current_room
        self.item = []

    def move(self, direction):
        if direction == 'n':
            self.current_room = self.current_room.n_to
        elif direction == 'e':
            self.current_room = self.current_room.e_to
        elif direction == 'w':
            self.current_room = self.current_room.w_to
        elif direction == 's':
            self.current_room = self.current_room.s_to

    def pickup(self, item):
        self.item.append(item)
        self.current_room.item.remove(item)
        print(self.item)
        return (f"{self.name} pick up {item}")

    def drop(self, item):
        self.item.remove(item)
        self.current_room.item.append(item)
        print(self.item)
        return (f"{self.name} pick up {item}")
