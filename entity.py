import tcod

class Entity:
    def __init__(self, name, x, y, ch, color) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.c = ch
        self.col = color

    def draw(self, console) -> None:
        console.print(x=self.x+17, y=self.y, string=chr(self.c), fg=self.col)