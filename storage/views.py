from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.http import FileResponse, Http404

from .models import StoredFile
from .serializers import StoredFileSerializer


class FileUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        uploaded_file = request.FILES.get("file")

        if not uploaded_file:
            return Response(
                {"error": "No file provided"},
                status=status.HTTP_400_BAD_REQUEST
            )

        stored_file = StoredFile.objects.create(
            owner=request.user,
            file=uploaded_file,
            original_name=uploaded_file.name,
            size=uploaded_file.size
        )

        serializer = StoredFileSerializer(stored_file)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FileListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        files = StoredFile.objects.filter(
            owner=request.user
        ).order_by("-uploaded_at")

        serializer = StoredFileSerializer(files, many=True)
        return Response(serializer.data)


class FileDownloadView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, file_id):
        try:
            stored_file = StoredFile.objects.get(
                id=file_id,
                owner=request.user
            )
        except StoredFile.DoesNotExist:
            raise Http404("File not found")

        response = FileResponse(
            stored_file.file.open("rb"),
            as_attachment=True
        )
        response["Content-Disposition"] = (
            f'attachment; filename="{stored_file.original_name}"'
        )
        return response
class FileDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, file_id):
        try:
            stored_file = StoredFile.objects.get(
                id=file_id,
                owner=request.user
            )
        except StoredFile.DoesNotExist:
            raise Http404("File not found")

        # delete file from storage
        stored_file.file.delete(save=False)
        # delete DB record
        stored_file.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
