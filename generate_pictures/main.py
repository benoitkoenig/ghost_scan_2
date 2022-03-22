import bpy

from ghost_scan_2.generate_pictures.add_light import add_light
from ghost_scan_2.generate_pictures.clear_scene import clear_scene

def main():
    clear_scene()
    add_light()

main()
