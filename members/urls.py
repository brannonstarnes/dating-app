from django.urls import path
from .views import MemberRegistrationView

urlpatterns = [
    path('register/', MemberRegistrationView.as_view(), name='register'),
]