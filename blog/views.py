from django.shortcuts import render
from django.utils import timezone
from .models import Post, WorkExperience
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, WorkExperienceForm
from django.shortcuts import redirect


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def resume_view(request):
    return render(request, 'blog/resume_view.html')


def work_experience_list(request):
    work_experiences = WorkExperience.objects.filter(start_date__lte=timezone.now()).order_by('start_date')
    return render(request, 'blog/work_experience_list.html', {'work_experiences': work_experiences})


def work_experience_new(request):
    if request.method == "POST":
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            work_experience = form.save(commit=False)
            work_experience.uuid = request.user
            work_experience.start_date = timezone.now()
            work_experience.save()
            return redirect('resume/view', pk=work_experience.pk)
    else:
        form = WorkExperienceForm()
    return render(request, 'blog/work_experience_edit.html', {'form': form})
