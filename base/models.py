from django.contrib.auth.models import User
from django.db import models


class OmurInitials(models.Model):

    class Meta:
        verbose_name = "İlk"
        verbose_name_plural = "ilkler"

    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.commenter.username