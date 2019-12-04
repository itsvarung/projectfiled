from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('formfile_app/', include('formfile_app.urls')),
]
