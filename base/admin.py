from django.contrib import admin
from base.models import OmurInitials


@admin.register(OmurInitials)
class OmurInitials(admin.ModelAdmin):
    list_display = ("id", "commenter", "content", "created_at")
