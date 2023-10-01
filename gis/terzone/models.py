import random

from django.db import models
from django.contrib.gis.db import models as gis_mod
from django.db.models import Q
from django.dispatch import receiver
from django.db.models.signals import post_save


def random_string():
    return int(random.randint(10000000, 99999999))


class KindTerzone(models.Model):

    code = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TerzoneExist(models.Model):
    class Status(models.IntegerChoices):
        ARCHIVED = 1
        AVAILABLE = 0

    geo_key = models.IntegerField(
        null=False,
        default=random_string,
    )
    index = models.CharField(max_length=100)
    kind_terzone = models.ForeignKey(
        KindTerzone,
        on_delete=models.PROTECT,
        null=True,
        related_name="terzoneexist",
    )
    geom = gis_mod.PolygonField(srid=3857)
    geom_type = models.CharField(max_length=20)
    status = models.IntegerField(
            choices=Status.choices,
        )

    def __str__(self):
        return self.index


class PlanRegulation(models.Model):
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=1000)
    index = models.CharField(max_length=100, default='-')
    terzones = models.ManyToManyField(
        TerzoneExist,
        related_name="planregs",
    )
    kind_terzone = models.ForeignKey(
        KindTerzone,
        on_delete=models.CASCADE,
        related_name="planreg",
        null=True,
    )
    archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Planning regulation <{self.pk}, {self.name!r}>"


# signals django
@receiver(post_save, sender=PlanRegulation)
def on_order_save(instance: PlanRegulation, created: bool, **kwargs):

    if not created:
        return

# all terzone/ filter kind_terzone_id
    terzones_on_kind = (
        TerzoneExist
        .objects
        .filter(status=0, kind_terzone_id=instance.kind_terzone_id)
        .all()
    )
    for terzone in terzones_on_kind:
        try:
            (PlanRegulation
             .objects
             .filter(~Q(archived=True))
             .get(kind_terzone_id=instance.kind_terzone_id)
             .terzones.add(terzone)
             )
        except:
            PlanRegulation.objects.filter(pk=instance.pk).delete()