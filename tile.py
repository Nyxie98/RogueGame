import xml.etree.ElementTree as ET 

class Tile:
    def __init__(self, x, y, tile):
        self.x = x
        self.y = y
        self.tile = tile


def get_tile(file, id):
    tiles = ET.parse(file)
    itemroot = tiles.getroot()

    for item in itemroot.findall("object"):
        if item.get('id') == str(id):
            return item
