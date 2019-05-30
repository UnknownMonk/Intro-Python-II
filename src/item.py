class Item:
    def __init__(self, name, discription):
        self.name = name
        self.discription = discription

    def __repr__(self):
        return self.name
