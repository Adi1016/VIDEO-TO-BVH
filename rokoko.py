import bpy


class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "wm.toggle_properties"
    bl_label = "Toggle N Panel"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                with context.temp_override(area=area):
                    bpy.ops.wm.context_toggle(data_path="space_data.show_region_ui")
                break
        return {'FINISHED'}


def register():
    bpy.utils.register_class(SimpleOperator)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)


if __name__ == "__main__":
    register()

    # Test call
    bpy.ops.wm.toggle_properties()