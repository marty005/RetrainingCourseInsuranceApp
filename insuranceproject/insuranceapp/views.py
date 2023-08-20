import datetime

from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import EInsuranceProduct, LifeInsurance, Policyholder

def index(request):
    return HttpResponse("Insurance App!!!")


class PolicyholderModelMixin:
    model = Policyholder


class PolicyholderFormFieldsMixin:
    fields = [
        "first_name",
        "last_name",
        "birth_date",
        "personal_identification_number",
        "street_and_reference_number",
        "city",
        "postal_code",
        "email",
        "phone",
    ]


class PolicyholderListView(PolicyholderModelMixin, ListView):
    queryset = Policyholder.objects.order_by("last_name")


class PolicyholderDetailView(PolicyholderModelMixin, DetailView):
    pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        policyholder_isurance_list = []
        for insurance_product in EInsuranceProduct:
            policyholder_isurance_list.extend(insurance_product.value.objects.filter(policyholder=self.kwargs["pk"]))
        context["policyholder_isurance_list"] = policyholder_isurance_list
        return context


class PolicyholderCreateView(PolicyholderModelMixin, PolicyholderFormFieldsMixin, CreateView):
    def form_valid(self, form):
        form.instance.registration_date = datetime.date.today()
        return super().form_valid(form)


class PolicyholderUpdateView(PolicyholderModelMixin, PolicyholderFormFieldsMixin, UpdateView):
    pass


class PolicyholderDeleteView(PolicyholderModelMixin, DeleteView):
    success_url = reverse_lazy("insuranceapp:policyholder-list")


class LifeInsuranceModelMixin:
    model = LifeInsurance


class LifeInsuranceFormFieldsMixin:
    fields = [
        "policyholder",
        "valid_from_date",
        "valid_to_date",
        "sum_assured",
        "insured",
        "beneficiary",
    ]

class LifeInsuranceDetailView(LifeInsuranceModelMixin, DetailView):
    pass


class LifeInsuranceCreateView(LifeInsuranceModelMixin, LifeInsuranceFormFieldsMixin, CreateView):
    def get_initial(self):
        initial = super().get_initial()
        initial["policyholder"] = self.kwargs["policyholder_id"]
        return initial

    def form_valid(self, form):
        form.instance.contract_conclusion_date = datetime.date.today()
        return super().form_valid(form)


class LifeInsuranceUpdateView(LifeInsuranceModelMixin, LifeInsuranceFormFieldsMixin, UpdateView):
    pass


class LifeInsuranceDeleteView(LifeInsuranceModelMixin, DeleteView):
    def get_success_url(self):
        return reverse("insuranceapp:policyholder-detail", kwargs={"pk": self.object.policyholder.id})
