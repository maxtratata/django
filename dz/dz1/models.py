from django.db import models


class Log(models.Model):
    path = models.CharField(max_length=255)
    visited_at = models.DateTimeField(auto_now_add=True)
