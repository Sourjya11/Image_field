from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView
from .forms import PostForm
from django.urls import reverse_lazy
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'user.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'admin.html'
    success_url = reverse_lazy('user')