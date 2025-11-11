from rest_framework import serializers
from .models import Note


# PUBLIC_INTERFACE
class NoteSerializer(serializers.ModelSerializer):
    """Serializer for the Note model with validation rules."""

    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_title(self, value: str) -> str:
        """
        Ensure title is non-empty and within the max length constraints.
        """
        if value is None or not str(value).strip():
            raise serializers.ValidationError("Title must not be empty.")
        return value.strip()
