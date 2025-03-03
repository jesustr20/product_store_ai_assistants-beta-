from django.urls import path
from .views import (
    CustomerSupportView,
    FAQListView,
    ProductManagerView,
    ContentMarketingView
)

urlpatterns = [
    path("customer-support/", CustomerSupportView.as_view(), name="customer-support"),
    path("faqs/", FAQListView.as_view(), name="faq-list"),
    path("product-manager/", ProductManagerView.as_view(), name="product-manager"),
    path("content-marketing/", ContentMarketingView.as_view(), name="content-marketing"),
]