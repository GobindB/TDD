from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    # functional test == end to end test == Acceptance test
    # writing the user story:
    def test_can_start_a_list_and_get_it_later(self):

        # our user decides to check out our new online to do app
        self.browser.get('http://localhost:8000')

        # she observes the 'to-do' in the title
        self.assertIn('To-Do', self.browser.title)

        # the UI invites the user to enter a to-do item upon site arrival
        inputBox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputBox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # the user types in 'Apply for Neuralink & Google internship' into a text input box
        inputBox.send_keys('Apply for Neuralink & Google internship')

        # the user hits enter and now the page updates and lists this as an item on the to-do list
        inputBox.send_keys(Keys.ENTER)
        time.sleep(2)

        self.check_for_row_in_list_table(
            '1: Apply for Neuralink & Google internship')

        # the text box persists and asks user to enter another item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # after user hits enter page reloads again and now shows both items on the list
        self.check_for_row_in_list_table(
            '1: Apply for Neuralink & Google internship')

        self.check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly')

        # user sees that site has generated a unique URL alongside some explanatory text to show data persistence
        self.fail('Finish the test!')

        # user visits URL and sees all their data

        # user leaves page and ends session
        browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')
