import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import (
    EInsuranceProduct,
    HomeInsurance,
    LifeInsurance,
    Policyholder,
)


def base(request):
    return render(request, "insuranceapp/base.html")


def insurance_product_select(request, policyholder_id):
    return HttpResponseRedirect(reverse(f"insuranceapp:{request.POST['view_name_prefix']}-create", kwargs={"policyholder_id": policyholder_id}))


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
        insurance_product_list = [insurance_product.value for insurance_product in EInsuranceProduct]
        context["insurance_product_list"] = insurance_product_list
        policyholder_isurance_list = []
        for insurance_product in insurance_product_list:
            policyholder_isurance_list.extend(insurance_product.objects.filter(policyholder=self.kwargs["pk"]))
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


class InsuranceCreateView(CreateView):
    template_name = "insuranceapp/insurance_form.html"

    def get_initial(self):
        initial = super().get_initial()
        initial["policyholder"] = self.kwargs["policyholder_id"]
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["insurance_product_name"] = self.model.insurance_product_name
        return context

    def form_valid(self, form):
        form.instance.contract_date = datetime.date.today()
        return super().form_valid(form)


class InsuranceUpdateView(UpdateView):
    template_name = "insuranceapp/insurance_form.html"


class InsuranceDeleteView(DeleteView):
    template_name = "insuranceapp/insurance_confirm_delete.html"

    def get_success_url(self):
        return reverse("insuranceapp:policyholder-detail", kwargs={"pk": self.object.policyholder.id})


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


class LifeInsuranceCreateView(LifeInsuranceModelMixin, LifeInsuranceFormFieldsMixin, InsuranceCreateView):
    pass


class LifeInsuranceUpdateView(LifeInsuranceModelMixin, LifeInsuranceFormFieldsMixin, InsuranceUpdateView):
    pass


class LifeInsuranceDeleteView(LifeInsuranceModelMixin, InsuranceDeleteView):
    pass


class HomeInsuranceModelMixin:
    model = HomeInsurance


class HomeInsuranceFormFieldsMixin:
    fields = [
        "policyholder",
        "valid_from_date",
        "valid_to_date",
        "sum_assured",
        "street_and_reference_number",
        "city",
        "postal_code",
    ]

class HomeInsuranceDetailView(HomeInsuranceModelMixin, DetailView):
    pass


class HomeInsuranceCreateView(HomeInsuranceModelMixin, HomeInsuranceFormFieldsMixin, InsuranceCreateView):
    pass


class HomeInsuranceUpdateView(HomeInsuranceModelMixin, HomeInsuranceFormFieldsMixin, InsuranceUpdateView):
    pass


class HomeInsuranceDeleteView(HomeInsuranceModelMixin, InsuranceDeleteView):
    pass