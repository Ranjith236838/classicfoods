from django.urls import path
from . import views

app_name = 'web1'

urlpatterns = [
    path('', views.index, name = 'indexx_page'),
]