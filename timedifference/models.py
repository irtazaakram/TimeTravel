from django.utils.timezone import now

from django.db import models

# Create your models here.
class TimeModel(models.Model):
    owner_id = models.CharField(max_length=40)
    created_at = models.DateTimeField(default=now)

    class Meta:
        app_label = "timedifference"
        ordering = ["created_at", "id"]

    @classmethod
    def create_model(cls, user_id):
        new_model = cls.objects.create(owner_id=user_id)
        return new_model
