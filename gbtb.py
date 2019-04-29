#!/bin/env python3

from PIL import Image
from sys import argv
from os import makedirs, path

def main():
    TILE_SIZE = (8, 8)
    print("GBTileBreaker, a GameBoy Tile Map chopper by Studiosi (TW: @ITStudiosi)")
    print("Under MIT license (check LICENSE for more details)")
    if len(argv) != 2:
        print("Invalid number of arguments: gbtb.py file")
        return
    image_path = argv[1]
    try:
        original_image = Image.open(image_path)
        print(f"Image path: {image_path}")
        print(f"Image size: {original_image.size}")
        print(f"Tile size: {TILE_SIZE}")
        if original_image.size[0] % TILE_SIZE[0] != 0 or original_image.size[1] % TILE_SIZE[1] != 0:
            print("Invalid image or tile size")
            return
        else:
            print("Sizes are correct")
        original_name = path.splitext(path.basename(path.abspath(image_path)))[0] 
        directory = f"./{original_name}"
        abs_directory = path.abspath(directory)
        print(f"Saving tiles to {abs_directory}")
        try:
            makedirs(abs_directory)
        except OSError:
            print("Unable to create directory (permissions, invalid or already existing directory)")
            return
        n_tiles = 0
        for x in range(0, original_image.size[0], TILE_SIZE[0]):
            for y in range(0, original_image.size[1], TILE_SIZE[1]):
                n_tiles += 1
                new_image = original_image.crop((x, y, x + TILE_SIZE[0], y + TILE_SIZE[1]))
                new_image.save(path.join(abs_directory, f"{n_tiles}.bmp"))
        print(f"{n_tiles} tiles saved. Enjoy!")
    except IOError:
        print(f"Unable to open image {image_path}")
            
if __name__ == "__main__":
    main()