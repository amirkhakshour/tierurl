from django.test import TestCase
from django.shortcuts import reverse
from django.http.response import HttpResponseNotAllowed, HttpResponseBadRequest
from shortner.views import MESSAGE_INVALID_DATA_PARAMS
from shortner.models import ShortURL


# Create your tests here.
class ShortnerPageTestCase(TestCase):
    def setUp(self):
        self.base_url = reverse('shortner-page')
        self.test_url = 'https://dummy.com'

    def test_post_is_only_allowed(self):
        response = self.client.get(self.base_url)
        assert response.status_code == HttpResponseNotAllowed.status_code

    def test_url_in_post_data_is_mandatory(self):
        response = self.client.post(self.base_url)
        assert response.status_code == HttpResponseBadRequest.status_code
        assert response.content == MESSAGE_INVALID_DATA_PARAMS

    def test_returns_alphanumeric_string(self):
        response = self.client.post(self.base_url, {'url': self.test_url})
        response_json = response.json()  # tests for json response too
        self.assertIn('tiny_url', response_json)
        tiny_url = response_json['tiny_url'].rsplit('/', 1)[-1]
        assert tiny_url.isalnum()
