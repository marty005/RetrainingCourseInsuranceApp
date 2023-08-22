from django.urls import path

from . import views

app_name = "insuranceapp"
urlpatterns = [
    path("", views.PolicyholderListView.as_view()),
    path(
        "policyholders/", views.PolicyholderListView.as_view(), name="policyholder-list"
    ),
    path(
        "policyholder/create/",
        views.PolicyholderCreateView.as_view(),
        name="policyholder-create",
    ),
    path(
        "policyholder/detail/<int:pk>/",
        views.PolicyholderDetailView.as_view(),
        name="policyholder-detail",
    ),
    path(
        "policyholder/update/<int:pk>/",
        views.PolicyholderUpdateView.as_view(),
        name="policyholder-update",
    ),
    path(
        "policyholder/delete/<int:pk>/",
        views.PolicyholderDeleteView.as_view(),
        name="policyholder-delete",
    ),
    path(
        "insurance-product/select/<int:policyholder_id>/",
        views.insurance_product_select,
        name="insurance-product-select",
    ),
    path(
        "lifeinsurance/create/<int:policyholder_id>/",
        views.LifeInsuranceCreateView.as_view(),
        name="lifeinsurance-create",
    ),
    path(
        "lifeinsurance/detail/<int:pk>/",
        views.LifeInsuranceDetailView.as_view(),
        name="lifeinsurance-detail",
    ),
    path(
        "lifeinsurance/update/<int:pk>/",
        views.LifeInsuranceUpdateView.as_view(),
        name="lifeinsurance-update",
    ),
    path(
        "lifeinsurance/delete/<int:pk>/",
        views.LifeInsuranceDeleteView.as_view(),
        name="lifeinsurance-delete",
    ),
    path(
        "homeinsurance/create/<int:policyholder_id>/",
        views.HomeInsuranceCreateView.as_view(),
        name="homeinsurance-create",
    ),
    path(
        "homeinsurance/detail/<int:pk>/",
        views.HomeInsuranceDetailView.as_view(),
        name="homeinsurance-detail",
    ),
    path(
        "homeinsurance/update/<int:pk>/",
        views.HomeInsuranceUpdateView.as_view(),
        name="homeinsurance-update",
    ),
    path(
        "homeinsurance/delete/<int:pk>/",
        views.HomeInsuranceDeleteView.as_view(),
        name="homeinsurance-delete",
    ),
]
