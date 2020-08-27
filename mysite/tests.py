from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
import blog.views

class ResumePageTest(TestCase):

    def test_root_url_resolves_to_resume_view(self):
        found = resolve('/resume')
        self.assertEqual(found.func, blog.views.resume_view)


