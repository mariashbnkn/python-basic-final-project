from django.urls import path
# from django.conf.urls import url

from .views import (
    TerzoneIndexView,
    TerzonesView,
    PlanregCreateView,
    KindTerzoneCreateView,
    KindTerzoneView,
    PlanregDetailView,
    PlanRegsListView,
    PlanregUpdateView,
    PlanregDeleteView,
    TerzoneDetailView,
)
from .geoserver import terzones_map

app_name = "terzone"

urlpatterns = [
    path("", TerzoneIndexView.as_view(), name="index"),
    path("terzones/", TerzonesView.as_view(), name="terzones"),
    path("terzones/<int:pk>/", TerzoneDetailView.as_view(), name="terzone"),
    path("terzones/terzones_map/", terzones_map, name="terzones_map"),
    path("planregs/", PlanRegsListView.as_view(), name="planregs"),
    path("planregs/<int:pk>/", PlanregDetailView.as_view(), name="planreg"),
    path("planregs/create/", PlanregCreateView.as_view(), name="create-planreg"),
    path("planregs/<int:pk>/update/", PlanregUpdateView.as_view(), name="update-planreg"),
    path("planregs/<int:pk>/confirm-delete/", PlanregDeleteView.as_view(), name="confirm-delete-planreg"),
    path("planregs/create/kindterzone/", KindTerzoneView.as_view(), name="kindterzone"),
    path("planregs/create/kindterzone/create/", KindTerzoneCreateView.as_view(), name="create-kindterzone"),
]
