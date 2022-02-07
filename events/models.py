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

    name = models.CharField(max_length=140)
    author = models.CharField(max_length=140)
    description = models.TextField()
    summary = models.CharField(max_length=140)
    capacity = models.PositiveSmallIntegerField(default=1)

    date = models.DateField(null=True, blank=True)
    start = models.TimeField(null=True, blank=True)
    end = models.TimeField(null=True, blank=True)

    is_online_event = models.BooleanField(default=True)
    is_invite_only = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])