from django.urls import path
from gcp_app import views


urlpatterns = [
    path("sample",views.sample)
]