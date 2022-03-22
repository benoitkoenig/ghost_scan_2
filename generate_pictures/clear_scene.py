import bpy

def clear_scene():
    while len(bpy.data.cameras) != 0:
        bpy.data.cameras.remove(bpy.data.cameras[0])
    while len(bpy.data.lights) != 0:
        bpy.data.lights.remove(bpy.data.lights[0])
    while len(bpy.data.materials) != 0:
        bpy.data.materials.remove(bpy.data.materials[0])
    while len(bpy.data.meshes) != 0:
        bpy.data.meshes.remove(bpy.data.meshes[0])
