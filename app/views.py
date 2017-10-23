from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from app.serializers import FileSerializer

class FileUploadView(APIView):
    def put(self, request):
        data = JSONParser().parse(request)
        serializer = FileSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)