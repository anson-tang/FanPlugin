import bpy
import bmesh

class MoveFacesAlongNormalsOperator(bpy.types.Operator):
    '''Move the faces along individual normal vectors.'''
    bl_idname = "fan.move_faces_along_normals_operator"
    bl_label = "Move Faces Along Normals"
    bl_options = {'REGISTER', 'UNDO'}
    
    distance = bpy.props.FloatProperty(name="Distance")

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.object.mode == 'EDIT'

    def execute(self, context):
        bm = bmesh.from_edit_mesh(context.object.data)
        for face in bm.faces:
            if face.select:
                normal = face.normal
                for vertex in face.verts:
                    vertex.co.x += normal.x * self.distance
                    vertex.co.y += normal.y * self.distance
                    vertex.co.z += normal.z * self.distance
        context.area.tag_redraw()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(MoveFacesAlongNormalsOperator)

def unregister():
    bpy.utils.unregister_class(MoveFacesAlongNormalsOperator)

if __name__ == "__main__":
    register()
