from http import HTTPStatus

from django.db.models import Q
from django.test import TestCase
from django.urls import reverse

from terzone.models import TerzoneExist


class TerzonesListViewTestCase(TestCase):
    fixtures = [
        "kindterzone-fixture.json",
        "terzone-fixture.json",
    ]

    def test_ok(self):
        url = reverse("terzone:terzones")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "terzone/terzones.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        terzones_qs = (
            TerzoneExist
            .objects
            .filter(~Q(status=TerzoneExist.Status.ARCHIVED))
            .order_by("kind_terzone_id")
            .only("id")
            .all()
        )
        self.assertQuerySetEqual(
            qs=terzones_qs,
            values=(p.pk for p in response.context["terzones"]),
            transform=lambda p: p.pk,
        )
