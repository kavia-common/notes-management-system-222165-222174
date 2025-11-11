from django.db import models


class Note(models.Model):
    """
    Note model representing a simple note entity.
    """
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # newest first by default

    def __str__(self) -> str:
        return f"{self.title[:50]}"
