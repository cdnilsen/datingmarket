from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("yentas/", include("yentas.urls")),
    path("admin/", admin.site.urls),
]