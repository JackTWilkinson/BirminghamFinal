from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve
from django.utils import timezone

from blog.forms import WorkExperienceForm, InterestForm
from blog.views import work_experience_list
from .models import Interest, WorkExperience


def create_test_interest(title='Testing Driven Development', description='I enjoy safe development', *test_user):
    return Interest(author=test_user, title=title, description=description)


def create_test_work_experience(
        *test_user, title='A tester', company='Test Co.', description='fun job', start_date=timezone.now()
):
    return WorkExperience(
        author=test_user, title=title, company=company, description=description, start_date=start_date
    )


class ResumeUnitTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')

    def test_user_instance(self):
        self.assertEqual(isinstance('', User))

    def test_url_resolves_to_resume_view(self):
        found = resolve('/resume/view')
        self.assertEqual(found.func, work_experience_list)

    def test_resume_view_uses_template(self):
        response = self.client.get('/resume/view')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'blog/resume_view.html')

    def test_resume_add_work_experience_valid(self):
        response = self.client.get('/work_experience/new')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'blog/work_experience_edit.html', 'blog/base.html')

    def test_resume_add_interest_valid(self):
        response = self.client.get('/interest/new/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'blog/interest_edit.html', 'blog/base.html')

    def test_interest_creation(self):
        interest = create_test_interest()
        self.assertTrue(isinstance(interest, Interest))
        self.assertEqual(interest.__str__(), interest.title)

    def test_work_experience_creation(self):
        work_experience = create_test_work_experience()
        self.assertTrue(isinstance(work_experience, WorkExperience))
        self.assertEqual(work_experience.__str__(), work_experience.title)

    def test_work_experience_form(self):
        form = WorkExperienceForm(data={
            'title': 'testform',
            'company': 'testcompany',
            'description': 'testdesc',
            'start_date': '2020-01-01',
            'end_date': '2020-10-10',
        })
        self.assertFalse(form.errors)

    def test_interest_form(self):
        form = InterestForm(data={
            'title': 'testform',
            'description': 'testdesc',
        })
        self.assertFalse(form.errors)

    def test_post_interest_success(self):
        response = self.client.post(
            '/interest/new/', data=create_test_interest(self.user)
        )

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response['Location'], '/interest/')
