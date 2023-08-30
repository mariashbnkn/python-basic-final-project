from django.db.models import Q
from django.test import TestCase
from django.urls import reverse

from terzone.models import PlanRegulation, KindTerzone


class TestPlanregsListTestCase(TestCase):
    # def setUp(self) -> None:

    @classmethod
    def setUpClass(cls):
        cls.planreg = PlanRegulation.objects.create(
            name="unique-name",
            note="some note",
        )

    @classmethod
    def tearDownClass(cls):
        cls.planreg.delete()

    def test_get_planreg(self):
        qs = PlanRegulation.objects
        count = qs.count()
        self.assertEqual(count, 1)
        planreg = qs.get()
        self.assertEqual(planreg.pk, self.planreg.pk)

    def test_get_planreg_details(self):
        url = reverse("terzone:planreg", kwargs={"pk": self.planreg.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "terzone/planregulation_detail.html")
        self.assertContains(response, self.planreg.note)
        self.assertContains(response, self.planreg.name)
        self.assertContains(response, self.planreg.pk)
