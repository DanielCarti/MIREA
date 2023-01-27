from django.db import models

# Create your models here.
class KursPrediction:
    def __init__(self, image_base64, encoding):
        self.image_base64 = image_base64
        self.encoding = encoding
