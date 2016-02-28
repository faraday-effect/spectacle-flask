from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView

from models import db, User, Role, Course, Section

# class SectionAdmin(ModelView):
#     form_ajax_refs = {
#         'the_course': {
#             'fields': (Course.code, Course.name)
#         }
#     }
#
#     def __init__(self, session):
#         super(SectionAdmin, self).__init__(Section, session)

class UserAdmin(ModelView):
    form_ajax_refs = {
        'roles': {
            'fields': (Role.name,)
        }
    }
    inline_models = (Role, )
    column_list = ('email', 'roles')

admin = Admin()
for model in (Course, Role, Section):
     admin.add_view(ModelView(model, db.session, category='Models'))
# admin.add_view(SectionAdmin(db.session))
admin.add_view(UserAdmin(User, db.session))
