import random, perlin_noise, tile

class Region:
    def __init__(self, seed, wx, wy) -> None:
        self.seed = seed
        self.wx = wx
        self.wy = wy
        self.tiles = []

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