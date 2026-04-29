from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from .forms import PostForm, SignUpForm
from .models import Post

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'blog/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def home_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required(login_url=reverse_lazy('login'))
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})

@login_required(login_url=reverse_lazy('login'))
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

@login_required(login_url=reverse_lazy('login'))
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('home')

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'blog/delete_post.html', {'post': post})
