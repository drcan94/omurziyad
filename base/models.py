from django.contrib.auth.models import User
from django.db import models


class OmurInitials(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
