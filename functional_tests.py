from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    # any method that starts with test_ is a test method - it'll be run by the tester.
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Let's see if the website is available - homepage:
        self.browser.get('http://localhost:8000')

        # Check and make sure the title and header are right:
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Invite the user to enter data into a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # User inputs data:
        inputbox.send_keys('Complete SI 699 Homework')
        # User selects and presses their <enter> key:
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1) # explicit wait - allows browser to complete operations

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Complete SI 699 Homework' for row in rows),
            "New to-do item did not appear in table" #add a failure message
        )
        # Another text box inviting user to add more data.
        # Page updates again.
        self.fail('Finish writing the test.')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
# Invite to enter/create a to-do item right away
# User inputs data into a text box
# When the user hits enter, the page updates and lists:
# 1: <User input data>

# There is still a text box inviting the user to add more input.
# User adds data, and the page updates again.

# The site will remember the user data. (Unique URL)
