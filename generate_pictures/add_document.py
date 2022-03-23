import bpy

def add_document():
    bpy.ops.mesh.primitive_plane_add()
    plane_object = bpy.data.objects["Plane"]
    plane_object.data.vertices[0].co = (-1.05, -1.475, 0)
    plane_object.data.vertices[1].co = (+1.05, -1.475, 0)
    plane_object.data.vertices[2].co = (-1.05, +1.475, 0)
    plane_object.data.vertices[3].co = (+1.05, +1.475, 0)
