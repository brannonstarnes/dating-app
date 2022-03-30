from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth import get_user_model
from .models import Member


class MemberCreationForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ("username", "email")


class MemberChangeForm(UserChangeForm):
    class Meta:
        model = Member
        fields = ("username", "email")
