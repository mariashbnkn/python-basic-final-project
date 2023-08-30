from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class TerzoneIndexViewTestCase(TestCase):

    def test_index_view_status_ok(self):
        url = reverse("terzone:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "terzone/index.html")
