from django.db import models
from django.utils import timezone

from events.models import Event


class News(models.Model):
    title = models.CharField(max_length=5000)
    slug = models.SlugField(unique=True, max_length=5000)
    description = models.TextField(blank=True, null=True)

    body = models.TextField(blank=True, null=True)

    meta_tags = models.CharField(max_length=5000, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)

    event = models.ForeignKey(
        Event, on_delete=models.DO_NOTHING, blank=True, null=True)

    # created and modified fields
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(News, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title
    
