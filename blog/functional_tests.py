from django.contrib.auth.models import User
from selenium import webdriver
import unittest


class ResumeViewTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_static_resume_info(self):
        self.browser.get('http://localhost:8000')
        self.browser.get('http://localhost:8000/resume/view')
        self.assertIn("Jack's Resume", self.browser.title)
        header_text = self.browser.find_element_by_class_name('resume-base').text
        self.assertIn('Jack Thomas Wilkinson', header_text)

    if __name__ == '__main__':
        unittest.main(warnings='ignore')
