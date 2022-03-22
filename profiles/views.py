from msilib.schema import Shortcut
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Profile
from .permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import * 

class ProfileList(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


def profile_pic_view(request):

    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')

        else:
            form = ProfilePicForm()
        return render(request, 'profile_pic.html', {'form': form}) 

def success(request):
    return HttpResponse('Upload successful')