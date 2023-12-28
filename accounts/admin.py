from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import Create, Change, CustomUser

class Admin(UserAdmin):
    add_form = Create
    form = Change
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'middlename', 'email', 'age']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', )}),
    )

admin.site.register(CustomUser, Admin)