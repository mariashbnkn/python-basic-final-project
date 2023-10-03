from django.contrib import admin

from .models import (
    # TerzoneExist,
    PlanRegulation,
    KindTerzone
    )


# @admin.register(TerzoneExist)
# class TerzoneExistAdmin(admin.ModelAdmin):
#     list_display = "id", "index"
#     list_display_links = "id", "index"


@admin.register(PlanRegulation)
class PlanRegulationAdmin(admin.ModelAdmin):
    list_display = "id", "name", "note"
    list_display_links = "id", "name"


@admin.register(KindTerzone)
class KindTerzoneAdmin(admin.ModelAdmin):
    list_display = "id", "name"
    list_display_links = "id", "name"
