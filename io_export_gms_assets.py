import bpy


def write_some_data(context, filepath, use_some_setting):
    print("running write_some_data...")
    f = open(filepath, 'w', encoding='utf-8')
    f.write("Hello World %s" % use_some_setting)
    f.close()

    return {'FINISHED'}

def write_from_template():
    pass

def write_all():
    pass

# ExportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ExportGMSAssets(Operator, ExportHelper):
    """Export various Blender data to a GameMaker:Studio local asset package"""
    bl_idname = "export_scene.gms_assets"
    bl_label = "Export GM:Studio Asset Package"

    # ExportHelper mixin class uses this
    filename_ext = ".yymp"

    filter_glob = StringProperty(
            default="*.yymp",
            options={'HIDDEN'},
            maxlen=255,  # Max internal buffer length, longer would be clamped.
            )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.

    type = EnumProperty(
            name="Stuff to export",
            options={'ENUM_FLAG'},
            description="Choose what to export",
            items=(('SCN', "Scenes", "Export scenes as rooms"),
                   ('IMG', "Images", "Export images as sprites")),
            )

    def execute(self, context):
        return write_some_data(context, self.filepath, self.use_setting)


# Only needed if you want to add into a dynamic menu
def menu_func_export(self, context):
    self.layout.operator(ExportGMSAssets.bl_idname, text="GM:Studio Asset Package (*.yymp)")


def register():
    bpy.utils.register_class(ExportGMSAssets)
    bpy.types.INFO_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ExportGMSAssets)
    bpy.types.INFO_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()