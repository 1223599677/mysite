from django.contrib import admin

from .models import PrivateGenome


class PrivateGenomeAdmin(admin.ModelAdmin):
    list_display = ['id', 'sequence_file', 'annotation_file', 'owner',
                    'create_time', 'update_time']


admin.site.register(PrivateGenome, PrivateGenomeAdmin)
