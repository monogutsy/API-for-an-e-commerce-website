from django.contrib import admin
from django.urls import include, path

from products.views import ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("api/", include("products.urls")),
]
