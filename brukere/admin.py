from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = Turgåere

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (
            'city',
            'test'
        )}),
    )


admin.site.register(Turgåere,CustomUserAdmin)