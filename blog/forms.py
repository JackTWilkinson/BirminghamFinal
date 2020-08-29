from django import forms

from .models import Post, WorkExperience, Interest


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ('title', 'description',)


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ('title', 'company', 'description', 'start_date', 'end_date')
