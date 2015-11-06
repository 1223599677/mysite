from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth import get_user_model

User = get_user_model()


class TimeModel(models.Model):
    create_time = models.DateTimeField(
        'created at', auto_now_add=True, editable=False, null=True)
    update_time = models.DateTimeField(
        'updated at', auto_now=True, editable=False, null=True)

    class Meta:
        abstract = True


class PrivateGenome(TimeModel):
    document_file = models.FileField(help_text='ducument file is optional',
        upload_to='private_genome/', null=True, blank=True)
    sequence_file = models.FileField(upload_to='private_genome/')
    annotation_file = models.FileField(upload_to='private_genome/')
    owner = models.ForeignKey(
        User, editable=False, null=True, blank=True,
        related_name='%(app_label)s_%(class)s_owner')


@python_2_unicode_compatible
class VisitRecord(models.Model):
    create_time = models.DateTimeField(
        auto_now_add=True, editable=False, null=True)

    def __str__(self):
        return str(self.pk)
