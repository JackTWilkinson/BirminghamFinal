from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from blog.views import resume_view


class ResumeViewTest(TestCase):

    def test_url_resolves_to_resume_view(self):
        found = resolve('/resume/view')
        self.assertEqual(found.func, resume_view)

    def test_resume_view_uses_template(self):
        response = self.client.get('/resume/view')
        self.assertTemplateUsed(response, 'blog/resume_view.html')
