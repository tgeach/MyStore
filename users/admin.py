from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):

    search_fields = ('email', 'user_name', 'first_name')
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('id', 'email', 'user_name', 'first_name', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields' : ('email', 'user_name', 'first_name')}),
        ('Personal', {'fields' : ('about', 'start_date')}), 
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions', 'last_login')}), 
        )
    formfield_overrides = {CustomUser.about: {'widget' : Textarea(attrs={'rows': 10, 'cols': 40})}}
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

admin.site.register(CustomUser, UserAdminConfig)
