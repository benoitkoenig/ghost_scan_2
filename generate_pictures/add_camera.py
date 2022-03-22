import bpy

def add_camera():
    camera_data = bpy.data.cameras.new("Camera")
    camera_object = bpy.data.objects.new(name="Camera", object_data=camera_data)
    camera_object.location = (0, -2, 10)
    camera_object.rotation_euler = (0.1,0,0)
    bpy.context.collection.objects.link(camera_object)
