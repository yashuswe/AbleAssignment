from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .admin import Posts
from .forms import BlogForm, EditForm
from django.urls import reverse_lazy
# from django.http import HttpResponse
# from django.template import loader
# def home(request):
#     return render(request, 'home.html', { })

class HomeView(ListView):
    model = Posts
    template_name = 'home.html'
    ordering = ['-date_created']


class ArtDetailView(DetailView):
    model = Posts
    template_name = 'article_det.html'

class AddPostView(CreateView):
    model = Posts
    form_class = BlogForm
    template_name = 'add_post.html'

class UpdateBlog(UpdateView):
    model = Posts
    form_class  = EditForm
    template_name= 'update_post.html'


class DeletePostView(DeleteView):
    model = Posts
    template_name= 'delete_post.html'
    success_url = reverse_lazy('home')