from django.contrib import admin
from .models import Profile

# PROFILE DETALLADO
class ProfileAdmin(admin.ModelAdmin):
    list_display =('user','user_group')
    search_fields =('user__username', 'user__groups__name')
    list_filter = ['user__groups']  # Cambiado a lista


    def user_group(self, obj):
        return " - ".join([t.name for t in obj.user.groups.all().order_by('name')])

    user_group.short_description = 'Grupo'

admin.site.register(Profile, ProfileAdmin)


