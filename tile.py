from multiprocessing.dummy import Array
import xml.etree.ElementTree as ET 

class Tile:
    def __init__(self, x, y, tile) -> None:
        self.x = x
        self.y = y
        self.tile = tile


def get_tile(file, id) -> Array:
    tiles = ET.parse(file)
    itemroot = tiles.getroot()

    for item in itemroot.findall("object"):
        if item.get('id') == str(id):
            return item
