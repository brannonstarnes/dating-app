from django.urls import path
from .views import ProfileList, ProfileDetail

urlpatterns = [
    path("", ProfileList.as_view(), name="profile_list"),
    path("<int:pk>/", ProfileDetail.as_view(), name="profile_detail"),
]
