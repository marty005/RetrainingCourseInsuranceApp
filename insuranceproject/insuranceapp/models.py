from enum import Enum

from django.db import models
from django.urls import reverse


class PersonBaseInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    personal_identification_number = models.IntegerField(unique=True)
    street_and_reference_number = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.IntegerField()

    class Meta:
        abstract = True

    @property
    def address(self):
        return f"{self.street_and_reference_number} {self.city}, {self.postal_code}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name


class Policyholder(PersonBaseInfo):
    """
    Pojistník
    """
    # client_id = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True)
    registration_date = models.DateField()

    def get_absolute_url(self):
        return reverse("insuranceapp:policyholder-detail", kwargs={"pk": self.id})


class Insured(PersonBaseInfo):
    """
    Pojištěný
    """


class Beneficiary(PersonBaseInfo):
    """
    Oprávněná osoba
    """

    class Meta:
        verbose_name_plural = "beneficiaries"


class InsuraceBaseInfo(models.Model):
    policyholder = models.ForeignKey(Policyholder, on_delete=models.CASCADE)
    # contract_id = models.IntegerField(unique=True)
    contract_conclusion_date = models.DateField()
    valid_from_date = models.DateField()
    valid_to_date = models.DateField()

    class Meta:
        abstract = True


class LifeInsurance(InsuraceBaseInfo):
    sum_assured = models.IntegerField() # Pojistná částka
    insured = models.ForeignKey(Insured, on_delete=models.CASCADE, blank=True, null=True)
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def insurance_product_name(self):
        return "Life Insurance"

    def get_absolute_url(self):
        return reverse("insuranceapp:lifeinsurance-detail", kwargs={"pk": self.id})


class EInsuranceProduct(Enum):
    LIFE_INSURANCE = LifeInsurance