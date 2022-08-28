import region

class World:
    def __init__(self, seed, sx, sy) -> None:
        self.seed = seed
        self.sx = sx
        self.sy = sy
        self.regions = []

    def generate_world(self) -> None:
        reg = region.Region(self.seed, 0, 0)
        reg.generate_region()
        self.regions.append(reg)