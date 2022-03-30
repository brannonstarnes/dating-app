from msilib.schema import Shortcut
from pdb import post_mortem
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Profile
from .permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .forms import * 

class ProfileList(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    

class ProfileDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Profile.objects.all()
    template_name = 'profile_detail.html'
    serializer_class = ProfileSerializer


class HomePageView(ListView):
    model = Profile
    template_name = 'home.html'
    context_object_name = 'all_profiles_list'

class CreateProfile(CreateView):
    model = Profile
    template_name = 'create_profile.html'
    fields = '__all__'

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