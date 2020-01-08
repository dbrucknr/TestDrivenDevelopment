from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    # any method that starts with test_ is a test method - it'll be run by the tester.
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
# Invite to enter/create a to-do item right away
# User inputs data into a text box
# When the user hits enter, the page updates and lists:
# 1: <User input data>

# There is still a text box inviting the user to add more input.
# User adds data, and the page updates again.

# The site will remember the user data. (Unique URL)
