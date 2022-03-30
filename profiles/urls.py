from django.urls import path
from .views import HomePageView, ProfileList, ProfileDetail, CreateProfile
from profiles.views import profile_pic_view, success

urlpatterns = [
    path("", ProfileList.as_view(), name="profile_list"),
    path("home/", HomePageView.as_view(), name="home"),
    path("create/", CreateProfile.as_view(), name="create_profile"),
    path("<int:pk>/", ProfileDetail.as_view(), name="profile_detail"),
    path("image_upload/", profile_pic_view, name = 'profile_pic_upload'),
    path("success/", success, name = 'success'),
]
