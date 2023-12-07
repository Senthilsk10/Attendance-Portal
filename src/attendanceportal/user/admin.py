from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,subject,attendance_pool,attendance,attendance_request


#
#class CustomUserAdmin(UserAdmin):
#    Fieldsets = (
#        *UserAdmin.fieldsets,
#        (
#            'Additional info',
#            {
#                'fields':(
#                    'dept',
#                    'role',
#                    'userid',
#                )
#            }
#        )
#    )
#
#admin.site.register(User, UserAdmin)

fields = list(UserAdmin.fieldsets)
fields[1] = ("personal info",{'fields':("first_name","last_name","email","dept","role","userid","sem")})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(User,UserAdmin)
admin.site.register(subject)
admin.site.register(attendance_pool)
admin.site.register(attendance)
admin.site.register(attendance_request)