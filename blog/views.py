from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Posts
from django.views.generic import (
    ListView, 
    DetailView, 
    UpdateView,
    CreateView,
    DeleteView
)

pagNum = 1

def about(request):
    return render(request, 'blog/about.html', {})

class PostListView(ListView):
    model = Posts
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = pagNum
 
class UserPostListView(ListView):
    model = Posts
    template_name = 'blog/UserPosts.html'
    context_object_name = 'posts'
    paginate_by = pagNum

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(author=user).order_by('-date_posted')

class CatPostListView(ListView):
    model = Posts
    template_name = 'blog/CatPosts.html'
    context_object_name = 'posts'
    paginate_by = pagNum

    def get_queryset(self):
        return Posts.objects.filter(deyCategory=self.kwargs.get('deyCategory')).order_by('-date_posted') 

class PostDetailView(DetailView):
    model = Posts
    template_name = 'blog/details.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts 
    template_name = 'blog/form.html'
    fields = ['title', 'content', 'image']
    # fields = ['title', 'deyCategory', 'content', 'image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts 
    template_name = 'blog/form.html'
    fields = ['title', 'content', 'image']
    # fields = ['title', 'deyCategory', 'content', 'image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def Blogdetails(request, myId):
    obj = get_object_or_404(Posts, id=myId)
    context={ 
        'post':obj,
        'title': obj.title
    }
    return render(request, 'blog/details.html', context)

