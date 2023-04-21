from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post, WebResource, Question


# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'stp_resources/home.html', context=context)


class PostListView(ListView):
    model = Post
    template_name = 'stp_resources/home.html'   # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    # This reverses the order so that newest is on top
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'stp_resources/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:  # type: ignore
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:  # type: ignore
            return True
        return False


def about(request):
    return render(request, 'stp_resources/about.html', {'title': 'About'})


def student_resource(request):
    context = {
        'studentResources': list(resource for resource in WebResource.objects.all() if resource.tag == "Student"),
        "questions": list(question for question in Question.objects.all() if question.tag == "Student"),
        'title': "Resources for Students",
    }
    return render(request, "stp_resources/student_resource.html", context)


def parent_resource(request):
    context = {
        'parentResources': list(resource for resource in WebResource.objects.all() if resource.tag == "Parent"),
        "questions": list(question for question in Question.objects.all() if question.tag == "Parent"),
        'title': "Resources for Parents",
    }

    return render(request, 'stp_resources/parent_resource.html', context)


def teacher_resource(request):
    context = {
        'teacherResources': list(resource for resource in WebResource.objects.all() if resource.tag == "Teacher"),
        "questions": list(question for question in Question.objects.all() if question.tag == "Teacher"),
        'title': "Resources for Teachers",
    }

    return render(request, 'stp_resources/teacher_resource.html', context)
