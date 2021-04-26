from django.db import models

# Create your models here.

class Notification(models.Model):
    name = models.CharField(max_length=200)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name