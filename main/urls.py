from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name="home"),
    path('subscribe/', views.add_email, name="add-email"),
    path('validate/', views.email_validation, name="validate_email"),
]
