import xml.etree.ElementTree as ET 
import tcod, math, random
import entity, world

WIDTH, HEIGHT = 60,40

KEY_COMMANDS = {
    tcod.event.KeySym.UP: "N",
    tcod.event.KeySym.DOWN: "S",
    tcod.event.KeySym.LEFT: "W",
    tcod.event.KeySym.RIGHT: "E"
}

def gen() -> tcod.bsp.BSP:
    bsp = tcod.bsp.BSP(x=17,y=1,width=44,height=25)
    bsp.split_recursive(
        depth = 5,
        min_width = 3,
        min_height = 3,
        max_horizontal_ratio = 1.5,
        max_vertical_ratio = 1.5
    )

    return bsp

world = world.World(123, 1, 1)
world.generate_world()
room = world.regions[0]

def main() -> None:
    tileset = tcod.tileset.load_tilesheet("LCD_Tileset.png", 16, 16, tcod.tileset.CHARMAP_CP437,)

    console = tcod.Console(WIDTH, HEIGHT, order="F")
    console2 = tcod.Console(42, 23, order="F")

    bsp = gen()

    player = entity.Entity("player", 10, 10, 64, (255,255,255))

    items = ET.parse("info/items.xml")
    itemroot = items.getroot()

    with tcod.context.new(columns = console.width, rows = console.height, tileset=tileset,) as context:
        while True:
            console.clear()
            console2.clear()

            console.draw_frame(x=0,y=0,width=16,height=40,title="Details",)
            console.draw_frame(x=16,y=0,width=44,height=25,)
            console.print_rect(x=17,y=0,width=16,height=1,string=" View ",)
            console.draw_frame(x=16,y=25,width=44,height=15,)
            console.print_rect(x=17,y=25,width=16,height=1,string=" Information ",)

            for j in range(0, len(room.tiles)):
                i = room.tiles[j]
                for part in i.tile.findall("part"):
                    if part.get("name") == "Render":
                        ch = part.get("render")
                        col = (int(part.get("r")), int(part.get("g")), int(part.get("b")))
                        console2.print(i.x, i.y, ch, fg=col)

            player.draw(console2)

            console2.blit(console, 17, 1)

            context.present(console)

            for event in tcod.event.wait():
                context.convert_event(event)

                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()
                elif isinstance(event, tcod.event.KeyDown):
                    if event.sym in KEY_COMMANDS:
                        match KEY_COMMANDS[event.sym]:
                            case "N":
                                player.y -= 1
                            case "S":
                                player.y += 1
                            case "W":
                                player.x -= 1
                            case "E":
                                player.x += 1


if __name__ == "__main__":
    main()