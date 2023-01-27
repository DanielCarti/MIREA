from rest_framework import serializers
from MIREA.func_app.views import encode_image
from MIREA.api.models import kurs_prediction

class ImageFromPillowSerializer(serializers.Serializer):
    image_base64 = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    encoding = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)