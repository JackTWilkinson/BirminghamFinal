from django.utils import timezone
from .models import Post, WorkExperience, Interest
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .forms import PostForm, WorkExperienceForm, InterestForm
from django.shortcuts import redirect
from django.views.generic.edit import DeleteView


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


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect('/')
    return render(request, 'blog/post_delete.html')


def resume_view(request):
    return render(request, 'blog/resume_view.html')


def work_experience_detail(request, pk):
    work_experience = get_object_or_404(WorkExperience, pk=pk)
    return render(request, 'blog/work_experience_detail.html', {'work_experience': work_experience})


def work_experience_list(request):
    work_experiences = WorkExperience.objects.filter(start_date__lte=timezone.now()).order_by('start_date')
    interests = Interest.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/work_experience_list.html', {
        'work_experiences': work_experiences,
        'interests': interests
    })


def work_experience_new(request):
    if request.method == "POST":
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            work_experience = form.save(commit=False)
            work_experience.uuid = request.user
            work_experience.start_date = timezone.now()
            work_experience.save()
            return redirect('work_experience_detail', pk=work_experience.pk)
    else:
        form = WorkExperienceForm()
    return render(request, 'blog/work_experience_edit.html', {'form': form})


def work_experience_edit(request, pk):
    work_experience = get_object_or_404(WorkExperience, pk=pk)
    if request.method == "POST":
        form = WorkExperienceForm(request.POST, instance=work_experience)
        if form.is_valid():
            work_experience = form.save(commit=False)
            work_experience.uuid = request.user
            work_experience.start_date = timezone.now()
            work_experience.save()
            return redirect('work_experience_detail', pk=work_experience.pk)
    else:
        form = WorkExperienceForm(instance=work_experience)
    return render(request, 'blog/work_experience_edit.html', {'form': form})


def work_experience_delete(request, pk):
    work_experience = get_object_or_404(WorkExperience, pk=pk)
    if request.method == "POST":
        work_experience.delete()
        return HttpResponseRedirect('/resume/view')
    return render(request, 'blog/work_experience_delete.html')


def interest_new(request):
    if request.method == "POST":
        form = InterestForm(request.POST)
        if form.is_valid():
            interest = form.save(commit=False)
            interest.author = request.user
            interest.published_date = timezone.now()
            interest.save()
            return redirect('interest_detail', pk=interest.pk)
    else:
        form = InterestForm()
    return render(request, 'blog/interest_edit.html', {'form': form})


def interest_detail(request, pk):
    interest = get_object_or_404(Interest, pk=pk)
    return render(request, 'blog/interest_detail.html', {'interest': interest})


def interest_edit(request, pk):
    interest = get_object_or_404(Interest, pk=pk)
    if request.method == "POST":
        form = InterestForm(request.POST, instance=interest)
        if form.is_valid():
            interest = form.save(commit=False)
            interest.author = request.user
            interest.published_date = timezone.now()
            interest.save()
            return redirect('interest_detail', pk=interest.pk)
    else:
        form = InterestForm(instance=interest)
    return render(request, 'blog/interest_edit.html', {'form': form})


def interest_delete(request, pk):
    interest = get_object_or_404(Interest, pk=pk)
    if request.method == "POST":
        interest.delete()
        return HttpResponseRedirect('/resume/view')
    return render(request, 'blog/interest_delete.html')
