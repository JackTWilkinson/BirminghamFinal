from django import forms

from .models import Post, WorkExperience


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ('title', 'company', 'description',)
