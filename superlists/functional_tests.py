from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    # functional test == end to end test == Acceptance test
    # writing the user story:
    def test_can_start_a_list_and_end_it_later(self):

        # our user decides to check out our new online to do app
        self.browser.get('http://localhost:8000')

        # she observes the 'to-do' in the title
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # the UI invites the user to enter a to-do item upon site arrival

        # the user types in 'apply for Neuralink & Google internship' into a text input box

        # the user hits enter and now the page updates and lists this as an item on the to-do list

        # the text box persists and asks user to enter another item

        # after user hits enter page reloads again and now shows both items on the list

        # user sees that site has generated a unique URL alongside some explanatory text to show data persistence

        # user visits URL and sees all their data

        # user leaves page and ends session
        browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')
