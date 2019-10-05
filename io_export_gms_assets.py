import bpy
import os
import uuid
import json
import shutil

sprite_template = {
    "id": "7764d253-2f87-44a4-84fb-b4142b18af16",
    "modelName": "GMSprite",
    "mvc": "1.12",
    "name": "sprite1",
    "For3D": False,
    "HTile": False,
    "VTile": False,
    "bbox_bottom": 54,
    "bbox_left": 13,
    "bbox_right": 56,
    "bbox_top": 5,
    "bboxmode": 0,
    "colkind": 1,
    "coltolerance": 0,
    "edgeFiltering": False,
    "frames": [
        {
            "id": "e8e292fa-5ce5-402b-9cc8-5d4b64ac7ef3",
            "modelName": "GMSpriteFrame",
            "mvc": "1.0",
            "SpriteId": "7764d253-2f87-44a4-84fb-b4142b18af16",
            "compositeImage": {
                "id": "93639865-2305-402d-94b2-e65f6fb3f803",
                "modelName": "GMSpriteImage",
                "mvc": "1.0",
                "FrameId": "e8e292fa-5ce5-402b-9cc8-5d4b64ac7ef3",
                "LayerId": "00000000-0000-0000-0000-000000000000"
            },
            "images": [
                {
                    "id": "19cc57e8-f6ce-472e-b446-7f51d9b19a27",
                    "modelName": "GMSpriteImage",
                    "mvc": "1.0",
                    "FrameId": "e8e292fa-5ce5-402b-9cc8-5d4b64ac7ef3",
                    "LayerId": "c2a7180a-6630-4a10-8f87-ebcc4b731a19"
                }
            ]
        }
    ],
    "gridX": 0,
    "gridY": 0,
    "height": 64,
    "layers": [
        {
            "id": "c2a7180a-6630-4a10-8f87-ebcc4b731a19",
            "modelName": "GMImageLayer",
            "mvc": "1.0",
            "SpriteId": "7764d253-2f87-44a4-84fb-b4142b18af16",
            "blendMode": 0,
            "isLocked": False,
            "name": "default",
            "opacity": 100,
            "visible": True
        }
    ],
    "origin": 0,
    "originLocked": False,
    "playbackSpeed": 15,
    "playbackSpeedType": 0,
    "premultiplyAlpha": False,
    "sepmasks": False,
    "swatchColours": None,
    "swfPrecision": 2.525,
    "textureGroupId": "1225f6b0-ac20-43bd-a82e-be73fa0b6f4f",
    "type": 0,
    "width": 64,
    "xorig": 0,
    "yorig": 0
}

room_template = {
    "name": "room0",
    "id": "dd7bc2f2-c205-44b2-ad33-f315760ca566",
    "creationCodeFile": "",
    "inheritCode": False,
    "inheritCreationOrder": False,
    "inheritLayers": False,
    "instanceCreationOrderIDs": [

    ],
    "IsDnD": False,
    "layers": [
        
    ],
    "modelName": "GMRoom",
    "parentId": "00000000-0000-0000-0000-000000000000",
    "physicsSettings": {
        "id": "419a3681-39c2-4ca5-ba6b-417315d3677d",
        "inheritPhysicsSettings": False,
        "modelName": "GMRoomPhysicsSettings",
        "PhysicsWorld": False,
        "PhysicsWorldGravityX": 0,
        "PhysicsWorldGravityY": 10,
        "PhysicsWorldPixToMeters": 0.1,
        "mvc": "1.0"
    },
    "roomSettings": {
        "id": "2211b4e3-c64a-4070-8374-54eb79afd871",
        "Height": 768,
        "inheritRoomSettings": False,
        "modelName": "GMRoomSettings",
        "persistent": False,
        "mvc": "1.0",
        "Width": 1024
    },
    "mvc": "1.0",
    "views": [
        {"id": "690b0ab4-7a3c-47b1-b305-e52022a4f2bb","hborder": 32,"hport": 768,"hspeed": -1,"hview": 768,"inherit": False,"modelName": "GMRView","objId": "00000000-0000-0000-0000-000000000000","mvc": "1.0","vborder": 32,"visible": True,"vspeed": -1,"wport": 1024,"wview": 1024,"xport": 0,"xview": 0,"yport": 0,"yview": 0},
        {"id": "0afd3f6a-92a5-4a55-9ad1-f43f3eb7f507","hborder": 32,"hport": 768,"hspeed": -1,"hview": 768,"inherit": False,"modelName": "GMRView","objId": "00000000-0000-0000-0000-000000000000","mvc": "1.0","vborder": 32,"visible": False,"vspeed": -1,"wport": 1024,"wview": 1024,"xport": 0,"xview": 0,"yport": 0,"yview": 0},
        {"id": "0b67286d-915f-47ab-9da4-58faa19cfb82","hborder": 32,"hport": 768,"hspeed": -1,"hview": 768,"inherit": False,"modelName": "GMRView","objId": "00000000-0000-0000-0000-000000000000","mvc": "1.0","vborder": 32,"visible": False,"vspeed": -1,"wport": 1024,"wview": 1024,"xport": 0,"xview": 0,"yport": 0,"yview": 0},
        {"id": "4b162613-9d1c-4434-8b53-467730054566","hborder": 32,"hport": 768,"hspeed": -1,"hview": 768,"inherit": False,"modelName": "GMRView","objId": "00000000-0000-0000-0000-000000000000","mvc": "1.0","vborder": 32,"visible": False,"vspeed": -1,"wport": 1024,"wview": 1024,"xport": 0,"xview": 0,"yport": 0,"yview": 0},
        {"id": "4964e98a-b5ab-497c-b81c-99ddce27a100","hborder": 32,"hport": 768,"hspeed": -1,"hview": 768,"inherit": False,"modelName": "GMRView","objId": "00000000-0000-0000-0000-000000000000","mvc": "1.0","vborder": 32,"visible": False,"vspeed": -1,"wport": 1024,"wview": 1024,"xport": 0,"xview": 0,"yport": 0,"yview": 0},
        {"id": "c2dbf919-f201-454b-8dba-49676042660d","hborder": 32,"hport": 768,"hspeed": -1,"hview": 768,"inherit": False,"modelName": "GMRView","objId": "00000000-0000-0000-0000-000000000000","mvc": "1.0","vborder": 32,"visible": False,"vspeed": -1,"wport": 1024,"wview": 1024,"xport": 0,"xview": 0,"yport": 0,"yview": 0},
        {"id": "daff8828-e6fa-4e3b-99ff-47651479aa4a","hborder": 32,"hport": 768,"hspeed": -1,"hview": 768,"inherit": False,"modelName": "GMRView","objId": "00000000-0000-0000-0000-000000000000","mvc": "1.0","vborder": 32,"visible": False,"vspeed": -1,"wport": 1024,"wview": 1024,"xport": 0,"xview": 0,"yport": 0,"yview": 0},
        {"id": "fbf101c0-c9bd-4d97-a35a-54d646684bb3","hborder": 32,"hport": 768,"hspeed": -1,"hview": 768,"inherit": False,"modelName": "GMRView","objId": "00000000-0000-0000-0000-000000000000","mvc": "1.0","vborder": 32,"visible": False,"vspeed": -1,"wport": 1024,"wview": 1024,"xport": 0,"xview": 0,"yport": 0,"yview": 0}
    ],
    "viewSettings": {
        "id": "1c1cced9-b318-4512-9015-f049526ca4c1",
        "clearDisplayBuffer": True,
        "clearViewBackground": False,
        "enableViews": True,
        "inheritViewSettings": False,
        "modelName": "GMRoomViewSettings",
        "mvc": "1.0"
    }
}

room_resource_template = {
    "id": "62522c3f-4329-4001-b737-0eb944d91555",
    "resourcePath": "rooms\\room1\\room1.yy",
    "resourceType": "GMRoom",
    "viewPath": "rooms"
}

sprite_resource_template = {
    "id": "7764d253-2f87-44a4-84fb-b4142b18af16",
    "resourcePath": "sprites\\sprite1\\sprite1.yy",
    "resourceType": "GMSprite",
    "viewPath": "sprites"
}

def write_some_data(context, filepath, publisher_name, display_name, version):
    # Extract names from path
    dir_fname = os.path.split(filepath)
    print(dir_fname)
    package_id = (os.path.splitext(dir_fname[1]))[0]
    
    # Create a temporary directory that we will zip later
    root_dir = dir_fname[0] + "/" + package_id
    os.mkdir(root_dir)
    os.chdir(root_dir)
    
    resource_data = []
    
    # Contents of "assetpackage.yy"
    package_data = {
        "description": None,
        "helpfile": None,
        "license": None,
        "name": display_name,
        "packageID": package_id,
        "packageType": "asset",
        "projectType": "",
        "publisherName": publisher_name,
        "resources": resource_data,
        "version": version
    }
    
    # Start with images/sprites
    os.mkdir("sprites")
    os.chdir("sprites")
    for img in bpy.data.images:
        img_desc = sprite_template.copy()
        resource_id = str(uuid.uuid4())
        frame_id = str(uuid.uuid4())
        layer_id = str(uuid.uuid4())
        
        if img.filepath == '':
            continue
        
        sprite_name = "spr_" + img.name
        
        sprite_res_data = sprite_resource_template.copy()
        sprite_res_data["name"] = sprite_name
        sprite_res_data["id"] = resource_id
        sprite_res_data["resourcePath"] = "sprites/" + sprite_name + "/" + sprite_name + ".yy"
        
        resource_data.append(sprite_res_data)
        
        img_desc["id"] = resource_id
        img_desc["name"] = sprite_name
        img_desc["premultiplyAlpha"] = True if img.alpha_mode == 'PREMUL' else False
        img_desc["width"] = img.size[0]
        img_desc["height"] = img.size[1]
        frame = img_desc["frames"][0]
        frame["id"] = frame_id
        frame["SpriteId"] = resource_id
        frame["compositeImage"]["FrameId"] = frame_id
        frame["compositeImage"]["id"] = str(uuid.uuid4())
        frame["images"][0]["FrameId"] = frame_id
        frame["images"][0]["LayerId"] = layer_id
        frame["images"][0]["id"] = str(uuid.uuid4())
        
        img_desc["layers"][0]["id"] = layer_id
        img_desc["layers"][0]["SpriteId"] = resource_id
        
        os.mkdir(sprite_name)
        os.chdir(sprite_name)
        
        f = open(sprite_name + ".yy", "w")
        
        json.dump(img_desc, f)
        
        f.close()
        
        img.save_render(frame_id + ".png")
        
        os.mkdir("layers")
        os.chdir("layers")
        
        os.mkdir(frame_id)
        os.chdir(frame_id)
        
        img.save_render(layer_id + ".png")
        
        os.chdir("..")
        
        os.chdir("..")
        
        os.chdir("..")
        
    os.chdir("..")
    
    # Or rather scenes/rooms
    os.mkdir("rooms")
    os.chdir("rooms")
    for scn in bpy.data.scenes:
        room_name = "rom_" + scn.name.lower()
        scn_desc = room_template.copy()
        print(scn_desc)
        scn_desc["name"] = room_name
        scn_desc["id"] = str(uuid.uuid4())
        
        room_res_data = room_resource_template.copy()
        room_res_data["id"] = scn_desc["id"]
        room_res_data["resourcePath"] = "rooms/" + room_name + "/" + room_name + ".yy"
        
        node = scn_desc["physicsSettings"]
        node["id"] = str(uuid.uuid4())
        node["PhysicsWorldGravityX"] = scn.gravity[0]
        node["PhysicsWorldGravityY"] = scn.gravity[1]
        node["PhysicsWorld"] = not(scn.rigidbody_world == None)
        
        node = scn_desc["roomSettings"]
        node["id"] = str(uuid.uuid4())
        
        node = scn_desc["viewSettings"]
        node["id"] = str(uuid.uuid4())
        
        node = scn_desc["views"]
        node_render = scn.render
        for view in node:
            view["id"] = str(uuid.uuid4())
            view["wport"] = node_render.resolution_x
            view["hport"] = node_render.resolution_y
        
        resource_data.append(room_res_data)
        
        os.mkdir(room_name)
        os.chdir(room_name)
        f = open(room_name + ".yy", "w")
        
        json.dump(scn_desc, f)
        
        f.close()
        
        os.chdir("..")
    os.chdir("..")
    
    # Or even better: models
    os.mkdir("datafiles")
    os.mkdir("datafiles_yy")
    os.chdir("datafiles")
    os.chdir("..")
    os.chdir("datafiles_yy")
    os.chdir("..")
    
    # Write resource list to package file
    f = open("assetpackage.yy", "w")
    
    json.dump(package_data, f)
    
    f.close()
    
    # Create zip file and change to .yymp
    os.chdir("..")
    if os.path.exists(package_id + ".yymp"):
        os.remove(package_id + ".yymp")
    shutil.make_archive(package_id, "zip", package_id)
    os.rename(package_id + ".zip", package_id + ".yymp")
    shutil.rmtree(package_id, ignore_errors=True)
    
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
    bl_options = {'PRESET'}
    
    # ExportHelper mixin class uses this
    filename_ext = ".yymp"
    
    filter_glob = StringProperty(
            default="*.yymp",
            options={'HIDDEN'},
            maxlen=255,  # Max internal buffer length, longer would be clamped.
            )
    
    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
    
    publisher_name = StringProperty(
        name="Publisher",
        description="Name of the publisher",
        default="",
    )
    
    display_name = StringProperty(
        name="Name",
        description="Display Name",
        default="",
    )
    
    version = StringProperty(
        name="Version",
        description="Version",
        default="1.0.0",
    )

    type = EnumProperty(
            name="Stuff to export",
            options={'ENUM_FLAG'},
            description="Choose what to export",
            items=(('SCN', "Scenes", "Export scenes as rooms"),
                   ('IMG', "Images", "Export images as sprites"),
                   ('CAM', "Cameras", "Export cameras to a script"),
                   ('MDL', "Models", "Export model data as vertex buffers in included files")),
            )

    def execute(self, context):
        return write_some_data(context, self.filepath, self.publisher_name, self.display_name, self.version)


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