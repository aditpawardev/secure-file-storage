from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class StoredFile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to="uploads/")
    original_name = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_name
