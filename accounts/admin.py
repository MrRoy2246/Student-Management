from django.contrib import admin
from .models import User
# Register your models here.
admin.site.register(User)

        # custom user model er joono  custom admin panel also  admin.site.register(User) works perfectly this is for future

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import User
# class UserAdmin(BaseUserAdmin):
#     list_display = ('email', 'full_name', 'role', 'is_active', 'is_staff', 'is_superuser')
#     list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')

#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal Info', {'fields': ('full_name', 'role')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important Dates', {'fields': ('last_login',)}),  # remove date_joined here
#     )

#     readonly_fields = ('last_login', 'date_joined')  # add date_joined here

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'full_name', 'role', 'password1', 'password2'),
#         }),
#     )

#     search_fields = ('email', 'full_name')
#     ordering = ('email',)


# admin.site.register(User, UserAdmin)
