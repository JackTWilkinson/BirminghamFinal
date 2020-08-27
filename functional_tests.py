from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_add_work_experience(self):
        # Assert that the base page and resume view work
        self.browser.get('http://localhost:8000')
        self.browser.get('http://localhost:8000/resume/view')

        # Assert the page title is correct
        self.assertIn("Jack's Resume", self.browser.title)


# Static part of the resume page is correctly displaying
# Bottom static of the page displays correctly

# User logs in and adds a new work experience

# User edits the work experience

# User deletes the work experience

# User creates an interest

# User edits an interest

# User deletes an interest

if __name__ == '__main__':
    unittest.main(warnings='ignore')
