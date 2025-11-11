# notes-management-system-222165-222174

Notes API (Django REST Framework)
- Base URL (preview): /api/
- Endpoints:
  - GET /api/notes/ — paginated list (count, next, previous, results), default order newest first
  - GET /api/notes/{id}/ — retrieve a single note
  - POST /api/notes/ — create { title: string (<=200, required), content: string }
  - PUT /api/notes/{id}/ — full update
  - PATCH /api/notes/{id}/ — partial update
  - DELETE /api/notes/{id}/ — delete
  - Search: /api/notes/?search=term — searches title and content (icontains)
  - Ordering override: /api/notes/?ordering=created_at or -created_at

Health
- GET /api/health/ — {"message": "Server is up!"}

Pagination
- Page size 10 by default; use ?page=2 for subsequent pages.

Swagger/Redoc
- /docs for Swagger UI (dynamic base)
- /redoc for ReDoc