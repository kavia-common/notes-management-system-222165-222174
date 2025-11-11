from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, permissions, filters
from rest_framework.request import Request

from .models import Note
from .serializers import NoteSerializer


@api_view(['GET'])
def health(request: Request) -> Response:
    """
    Health check endpoint.

    Returns:
        200 with {"message": "Server is up!"}
    """
    return Response({"message": "Server is up!"})


# PUBLIC_INTERFACE
class NoteViewSet(viewsets.ModelViewSet):
    """
    Notes CRUD API.

    Supports:
    - GET /api/notes/ (paginated list, newest first)
    - GET /api/notes/{id}/ (retrieve)
    - POST /api/notes/ (create)
    - PUT /api/notes/{id}/ (full update)
    - PATCH /api/notes/{id}/ (partial update)
    - DELETE /api/notes/{id}/ (delete)

    Query params:
    - search: searches title and content (icontains)
    - ordering: optional alternative ordering (default -created_at)
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at", "title"]
    ordering = ["-created_at"]  # default ordering
