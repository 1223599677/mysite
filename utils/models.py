from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth import get_user_model
import random
import string

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
    name = models.CharField(max_length=10, default='', help_text='private genome name')
    # !!! never use this field directly, use method `obj.get_random_string()`
    random_string = models.CharField(
        max_length=20, default='', blank=True, editable=False)

    def get_name(self):
        if not self.name:
            self.name = 'private genome {}'.format(self.pk)
            self.save()
        return self.name.replace(' ', '_')

    def get_random_string(self, length=5):
        if not self.random_string:
            self.random_string = ''.join(
                random.choice(string.letters+string.digits) for _ in range(length))
            self.save()
        return self.random_string + str(self.pk)

    def get_browse_url(self):
        url = ('http://genebrowser.lifemodules.org/jbrowse/?data='
               '{username}/{name}_{random_string}'
             ).format(
                username = self.owner.username,
                name = self.name,
                random_string = self.get_random_string()
             )
        return url


@python_2_unicode_compatible
class VisitRecord(models.Model):
    create_time = models.DateTimeField(
        auto_now_add=True, editable=False, null=True)

    def __str__(self):
        return str(self.pk)
