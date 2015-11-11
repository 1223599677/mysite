from django.contrib import admin

from .models import PrivateGenome, SequenceInfo


class PrivateGenomeAdmin(admin.ModelAdmin):
    list_display = ['id', 'sequence_file', 'annotation_file', 'owner',
                    'create_time', 'update_time']


class SequenceInfoAdmin(admin.ModelAdmin):
    list_display = ['strain', 'strain_owner', 'sequence_type', 'public_type',
    'industrial_application', 'document_file']


admin.site.register(PrivateGenome, PrivateGenomeAdmin)
admin.site.register(SequenceInfo, SequenceInfoAdmin)
