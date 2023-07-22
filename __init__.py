import os
import bpy
bl_info = {
    "name": "Victorian Asset Library Installer",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "description": "Adds a button to install Victorian Asset Library",
    "category": "Assets",
}


class VICTORIAN_OT_add_asset_library(bpy.types.Operator):
    bl_idname = "victorian.add_asset_library"
    bl_label = "Install Victorian Asset Library"
    bl_description = "Adds the Victorian asset library to Blender's asset browser"

    def execute(self, context):
        # Check if Victorian library already exists
        prefs = bpy.context.preferences
        for lib in prefs.filepaths.asset_libraries:
            if lib.name == "Victorian":
                self.report(
                    {'INFO'}, "Victorian Asset Library already installed!")
                return {'FINISHED'}

        # If the Victorian library doesn't exist, let's add it.
        bpy.ops.preferences.asset_library_add()
        new_lib = prefs.filepaths.asset_libraries[-1]

        # Set the name for the new library
        new_lib.name = "Victorian"

        # Use the path to the addon's directory to locate the assets.blend file
        current_addon_dir = os.path.dirname(os.path.realpath(__file__))
        assets_blend_path = os.path.join(current_addon_dir, "assets.blend")

        # Set the path for the new library
        new_lib.path = assets_blend_path

        self.report({'INFO'}, "Victorian Asset Library installed!")
        return {'FINISHED'}


class VICTORIAN_PT_asset_library_panel(bpy.types.Panel):
    bl_label = "Victorian Library"
    bl_idname = "VICTORIAN_PT_asset_library_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Victorian'

    def draw(self, context):
        layout = self.layout

        layout.operator(VICTORIAN_OT_add_asset_library.bl_idname)


def register():
    bpy.utils.register_class(VICTORIAN_OT_add_asset_library)
    bpy.utils.register_class(VICTORIAN_PT_asset_library_panel)


def unregister():
    bpy.utils.unregister_class(VICTORIAN_OT_add_asset_library)
    bpy.utils.unregister_class(VICTORIAN_PT_asset_library_panel)


if __name__ == "__main__":
    register()
