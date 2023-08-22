from enum import Enum

from django.db import models
from django.urls import reverse


class Person(models.Model):
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
    
    @property
    def personal_identification_number_as_string(self):
        return f"{str(self.personal_identification_number)[:6]}/{str(self.personal_identification_number)[6:]}"
    
    def __str__(self):
        return self.full_name


class Policyholder(Person):
    """
    Pojistník
    """
    # client_id = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True)
    registration_date = models.DateField()

    def get_absolute_url(self):
        return reverse("insuranceapp:policyholder-detail", kwargs={"pk": self.id})


class Insured(Person):
    """
    Pojištěný
    """


class Beneficiary(Person):
    """
    Oprávněná osoba
    """

    class Meta:
        verbose_name_plural = "beneficiaries"


class Insurace(models.Model):
    insurance_product_name = "Insurance"

    policyholder = models.ForeignKey(Policyholder, on_delete=models.CASCADE)
    # contract_id = models.IntegerField(unique=True)
    contract_date = models.DateField()
    valid_from_date = models.DateField()
    valid_to_date = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.insurance_product_name
    
    @classmethod
    def get_url_name_prefix(cls):
        return cls.insurance_product_name.replace(" ", "").lower()
    
    def get_absolute_url(self):
        return self.get_detail_url()

    def get_detail_url(self):
        return reverse(f"insuranceapp:{self.__class__.get_url_name_prefix()}-detail", kwargs={"pk": self.id})

    def get_update_url(self):
        return reverse(f"insuranceapp:{self.__class__.get_url_name_prefix()}-update", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse(f"insuranceapp:{self.__class__.get_url_name_prefix()}-delete", kwargs={"pk": self.id})


class LifeInsurance(Insurace):
    """
    Životní pojištění
    """
    insurance_product_name = "Life Insurance"

    sum_assured = models.IntegerField() # Pojistná částka
    insured = models.ForeignKey(Insured, on_delete=models.SET_NULL, blank=True, null=True)
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.SET_NULL, blank=True, null=True)


class HomeInsurance(Insurace):
    """
    Pojištění domácnosti
    """
    insurance_product_name = "Home Insurance"

    sum_assured = models.IntegerField() # Pojistná částka
    street_and_reference_number = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.IntegerField(blank=True, null=True)

    @property
    def address(self):
        return f"{self.street_and_reference_number} {self.city}, {self.postal_code}"


class EInsuranceProduct(Enum):
    HOME_INSURANCE = HomeInsurance
    LIFE_INSURANCE = LifeInsurance