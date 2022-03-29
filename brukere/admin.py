from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = Turgåere

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (
            'profilbilde',
            'by',
            'telefonnummer',
            'ferdighetsnivå',
            'seriøsaktør',
            'fødselsdato',
            'bedriftsaddresse',
        )}),
    )


admin.site.register(Turgåere,CustomUserAdmin)
admin.site.register(UpvotePoints)