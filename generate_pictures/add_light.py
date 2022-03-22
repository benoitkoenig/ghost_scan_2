import bpy

def add_light():
    light_data = bpy.data.lights.new("Main light", "POINT")
    light_object = bpy.data.objects.new(name="Main light", object_data=light_data)
    light_object.location = (1, 1, 10)
    bpy.context.collection.objects.link(light_object)
