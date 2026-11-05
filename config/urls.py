from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("app.dashboard.urls")),
    path("admin/", admin.site.urls),
]