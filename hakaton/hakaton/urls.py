from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('reg_editor.urls')),
    path("panel_re_editor", include('reg_editor.urls')),
    path("profile", include('reg_editor.urls')),
]
