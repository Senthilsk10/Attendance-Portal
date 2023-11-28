from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


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