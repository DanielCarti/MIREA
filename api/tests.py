from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from func_app.views import encode_image

# Create your tests here.

class kurs_prediction(APITestCase):
     def test_img_correct(self):
         base64_massage = encode_image(days=15,color='purple')
         url = reverse('image', args=[15,'purple'])
         response = self.client.get(url)
         self.assertEqual(response.data, {
             "image_base64": base64_massage,
             "encoding": 'utf-8'
         })