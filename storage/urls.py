from django.urls import path
from .views import (
    FileUploadView,
    FileListView,
    FileDownloadView,
    FileDeleteView,
)

urlpatterns = [
    path("upload/", FileUploadView.as_view(), name="file-upload"),
    path("", FileListView.as_view(), name="file-list"),
    path("<int:file_id>/download/", FileDownloadView.as_view(), name="file-download"),
    path("<int:file_id>/", FileDeleteView.as_view(), name="file-delete"),
]
