from django.urls import path

from . import views

app_name = "insuranceapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("policyholders/", views.PolicyholderListView.as_view(), name="policyholder-list"),
    path("policyholder/detail/<int:pk>/", views.PolicyholderDetailView.as_view(), name="policyholder-detail"),
    path("policyholder/create/", views.PolicyholderCreateView.as_view(), name="policyholder-create"),
    path("policyholder/update/<int:pk>/", views.PolicyholderUpdateView.as_view(), name="policyholder-update"),
    path("policyholder/delete/<int:pk>/", views.PolicyholderDeleteView.as_view(), name="policyholder-delete"),
    path("lifeinsurance/detail/<int:pk>/", views.LifeInsuranceDetailView.as_view(), name="lifeinsurance-detail"),
    path("lifeinsurance/create/<int:policyholder_id>/", views.LifeInsuranceCreateView.as_view(), name="lifeinsurance-create"),
    path("lifeinsurance/update/<int:pk>/", views.LifeInsuranceUpdateView.as_view(), name="lifeinsurance-update"),
    path("lifeinsurance/delete/<int:pk>/", views.LifeInsuranceDeleteView.as_view(), name="lifeinsurance-delete"),
]
