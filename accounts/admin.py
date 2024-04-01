from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ["email", "username", "age", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (("Extra", {"fields": ("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Extra", {"fields": ("age",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
