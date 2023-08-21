from django.contrib import admin

from .models import (
    Beneficiary,
    HomeInsurance,
    Insured,
    LifeInsurance,
    Policyholder,
)


admin.site.register(Beneficiary)
admin.site.register(HomeInsurance)
admin.site.register(Insured)
admin.site.register(LifeInsurance)
admin.site.register(Policyholder)