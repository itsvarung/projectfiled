from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('person_form/', views.PersonBasicDetailsFormView.as_view(), name='person_form'),
]