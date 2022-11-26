from django.urls import path

from . import views


urlpatterns = [
    path('core/signup', views.RegistrationView.as_view()),
    path('core/login', views.LoginView.as_view()),
]
