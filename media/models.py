from mimetypes import guess_type
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.files.base import ContentFile
from django.db import models


# Create your models here.
class Media(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    file = models.FileField(upload_to='media_files/')
    alt_text = models.CharField(max_length=255, blank=True)
    media_type = models.CharField(max_length=50, choices=[('image', 'Image'), ('video', 'Video')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_main = models.BooleanField(default=False)

    @staticmethod
    def get_upload_path(filename):
        mime_type, _ = guess_type(filename)
        if mime_type:
            type_main, _ = mime_type.split('/')
            if type_main == 'image':
                return 'images/' + filename
            elif type_main == 'video':
                return 'videos/' + filename
        # Default path if MIME type is not detected
        return 'others/' + filename

    def save(self, *args, **kwargs):
        if self.file:
            # Save the file to a new path based on MIME type
            new_file = ContentFile(self.file.read())
            self.file.save(self.get_upload_path(self.file.name), new_file, save=False)

        if self.is_main:
            # Ensure only one main media per object
            Media.objects.filter(content_type=self.content_type, object_id=self.object_id,
                                 media_type=self.media_type).update(is_main=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Media for {self.content_type} id {self.object_id}"
