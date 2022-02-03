import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Event(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])