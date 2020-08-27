from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class ResumeViewTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_static_resume_info(self):
        # Assert that the base page and resume view work
        self.browser.get('http://localhost:8000')
        self.browser.get('http://localhost:8000/resume/view')

        # Assert the page title is correct
        self.assertIn("Jack's Resume", self.browser.title)
        header_text = self.browser.find_element_by_id('name').text
        self.assertIn('Jack Thomas Wilkinson', header_text)
        work_experience = self.browser.find_element_by_id('work-experience')
        self.assertTrue(work_experience)

# User logs in and adds a new work experience

# User edits the work experience

# User deletes the work experience

# User creates an interest

# User edits an interest

# User deletes an interest

if __name__ == '__main__':
    unittest.main(warnings='ignore')
