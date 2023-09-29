from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView

from .forms import PlanregForm, KindTerzoneForm
from .models import PlanRegulation, TerzoneExist, KindTerzone


class TerzoneIndexView(TemplateView):
    template_name = "terzone/index.html"


class TerzonesView(View):
    template_name = "terzone/terzones.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        terzones = (
            TerzoneExist
            .objects
            .filter(~Q(status=TerzoneExist.Status.ARCHIVED))
            .order_by("kind_terzone_id")
            .all()
        )

        return render(
            request=request,
            template_name=self.template_name,
            context={
                "terzones": terzones,
            },
        )


class TerzoneDetailView(DetailView):
    model = TerzoneExist


class PlanRegsListView(ListView):
    queryset = (
        PlanRegulation
        .objects
        .filter(~Q(archived=True))
        .all()
    )


class PlanregCreateView(LoginRequiredMixin, CreateView):
    model = PlanRegulation
    form_class = PlanregForm
    success_url = reverse_lazy("terzone:planregs")


class PlanregDetailView(DetailView):
    model = PlanRegulation


# class PlanregTerzoneView(ListView):
#
#     def test_func(self):
#
#         # Order.objects.filter(...)
#         return self.request.user.is_staff
#
#     template_name = "terzone/planregulation_detail.html"
#     context_object_name = "planregs"
#     queryset = (
#         PlanRegulation
#         .objects
#         .order_by("id")
#         # .select_related("user", "payment_details")
#         .prefetch_related("terzones")
#         .all()
#     )


class PlanregUpdateView(UpdateView):
    template_name_suffix = "_update_form"
    model = PlanRegulation
    form_class = PlanregForm

    def get_success_url(self):
        return reverse("terzone:planreg", kwargs={"pk": self.object.pk})


class PlanregDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "terzone.delete_planreg"

    # model = Category
    success_url = reverse_lazy("terzone:planregs")
    queryset = (
        PlanRegulation
        .objects
        .filter(~Q(archived=True))
        .all()
    )

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return redirect(success_url)


class KindTerzoneView(View):
    template_name = "terzone/kindterzone.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        kind_terzones = (
            KindTerzone
            .objects
            .order_by("id")
            .all()
        )

        return render(
            request=request,
            template_name=self.template_name,
            context={
                "kind_terzones": kind_terzones,
            },
        )


class KindTerzoneCreateView(LoginRequiredMixin, CreateView):
    model = KindTerzone
    form_class = KindTerzoneForm
    success_url = reverse_lazy("terzone:kindterzone")