from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.generic import DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.

@user_passes_test(lambda u: u.is_authenticated)
def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect(post)
    context = {
        'form' : form
    }
    return render(request, 'blog/add_post.html', context)

def posts_home(request):
    context = {
        'posts': Post.objects.all().order_by("date_posted").reverse()
    }
    return render(request, 'blog/home.html', context)

@login_required()
def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.name = request.user.username
        comment.save()
        return redirect(request.path)
    form.initial["name"] = request.session.get('name')
    return render(request, 'blog/blog_post.html', {'post': post, 'form': form})

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model  = Post
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'text']

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

class UserPostView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/user_posts.html'
    paginate_by = 8
    
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')