import os
import bpy


class VICTORIAN_OT_add_asset_library(bpy.types.Operator):
    bl_idname = "victorian.add_asset_library"
    bl_label = "Install Victorian Asset Library"
    bl_description = "Adds the Victorian asset library to Blender's asset browser"

    # ... (rest of the code for this operator)
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
        assets_blend_path = os.path.join(
            current_addon_dir, "..", "library")

        # Set the path for the new library
        new_lib.path = assets_blend_path

        self.report({'INFO'}, "Victorian Asset Library installed!")
        return {'FINISHED'}


def _register():
    bpy.utils.register_class(VICTORIAN_OT_add_asset_library)


def _unregister():
    bpy.utils.unregister_class(VICTORIAN_OT_add_asset_library)
