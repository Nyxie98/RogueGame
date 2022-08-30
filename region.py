import random, perlin_noise, tile
from typing import List

class Region:
    def __init__(self, seed, wx, wy) -> None:
        self.seed = seed
        self.wx = wx
        self.wy = wy
        self.tiles = []

    def get_building_tiles(self) -> List:
        stiles = []

        for x in range(42):
            for y in range(23):
                suit = True
                ps = (y*42)+x
                
                for i in range(x, x+5):
                    for j in range(y, y+5):
                        pos = (j*42)+i

                        if i >= 42 or j >= 23:
                            suit = False
                        else:
                            for p in self.tiles[pos].tile.findall("part"):
                                if p.get("name") == "Physics" and p.get("solid") == "true":
                                    suit = False
                
                if suit == True:
                    stiles.append(ps)

        return stiles

    def generate_region(self) -> None:
        x = 0
        y = 0
        for i in range(0, 966):
            t = random.randrange(0,101)
            id = 0

            if (t <= 3): id = 5
            if (t> 3 and t <= 20): id = 3
            if (t > 20 and t <= 60): id = 4
            if (t > 60): id = 6
            
            nt = tile.Tile(x, y, tile.get_tile("info/items.xml",id))
            self.tiles.append(nt)

            x += 1

            if x == 42:
                x = 0
                y += 1

        noise = perlin_noise.PerlinNoise(octaves=3, seed=self.seed)
        xs = 42
        ys = 23

        pic = [[noise([i/xs, j/ys]) for j in range(xs)] for i in range(ys)]

        for i in range(xs):
            for j in range(ys):
                if (pic[j][i] > 0.1):
                    p = (j*xs)+i
                    self.tiles[p] = tile.Tile(i, j, tile.get_tile("info/items.xml",7))

        suitable_tiles = self.get_building_tiles()
        for t in suitable_tiles:
            self.tiles[t] = tile.Tile(self.tiles[t].x, self.tiles[t].y, tile.get_tile("info/items.xml",0))