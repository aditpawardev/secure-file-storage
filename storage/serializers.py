from rest_framework import serializers
from .models import StoredFile

class StoredFileSerializer(serializers.ModelSerializer):
   class Meta:
      model = StoredFile
      fields = '__all__'
