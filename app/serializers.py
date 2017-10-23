from rest_framework.serializers import ModelSerializer, FileField
from app.models import File


class FileSerializer(ModelSerializer):
    file = FileField()

    class Meta:
        model = File
        fields = ('file',)