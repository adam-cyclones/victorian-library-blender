import bpy


class VICTORIAN_PT_asset_library_panel(bpy.types.Panel):
    bl_label = "Victorian Library"
    bl_idname = "VICTORIAN_PT_asset_library_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Victorian'

    def draw(self, context):
        layout = self.layout
        layout.operator("victorian.add_asset_library")


def _register():
    bpy.utils.register_class(VICTORIAN_PT_asset_library_panel)


def _unregister():
    bpy.utils.unregister_class(VICTORIAN_PT_asset_library_panel)
