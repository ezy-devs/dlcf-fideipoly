from django.db import models


class Sermon(models.Model):
    title = models.CharField(max_length=200)
    preacher = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    audio_file = models.FileField(upload_to='sermons/audio/', blank=True, null=True)
    video_file = models.FileField(upload_to='sermons/video/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='sermons/covers/', blank=True, null=True)
    sermon_link = models.URLField(blank=True, null=True)
    sermon_notes = models.FileField(upload_to='sermons/notes/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title