from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Post, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreatePostForm, CreateCommentForm

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    login_url = 'login'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    login_url = 'login'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('title', 'body')
    template_name = 'post_update.html'
    login_url = 'login'
    

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    login_url = 'login'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    form_class = CreatePostForm
    login_url = 'login'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_new.html'
    form_class = CreateCommentForm
    login_url = 'login'

    def form_valid(self,form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs.get('pk')
        return super().form_valid(form)

def CategoryListView(request, category):
    category = category.capitalize()
    category_posts = Post.objects.filter(category = category)
    return render(request, 'category_list.html', {'category':category, 'category_posts':category_posts})

def SchoolListView(request, school):
    school_posts = Post.objects.filter(author__school = school)

    return render(
        request, 
        'school_list.html', 
        {'school':school, 'school_posts':school_posts}
    )
