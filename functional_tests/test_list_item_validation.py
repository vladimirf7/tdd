from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.ui import WebDriverWait
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        self.get_item_input_box().send_keys('Buy milk')
        self.get_item_input_box().send_keys(Keys.ENTER)
        WebDriverWait(self.browser, 10).until(expected_conditions
            .staleness_of(self.get_item_input_box()))
        self.check_for_row_in_list_table('1: Buy milk')
        self.get_item_input_box().send_keys(Keys.ENTER)
        WebDriverWait(self.browser, 10).until(expected_conditions
            .staleness_of(self.get_item_input_box()))

        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        self.get_item_input_box().send_keys('Make tea')
        self.get_item_input_box().send_keys(Keys.ENTER)
        WebDriverWait(self.browser, 10).until(expected_conditions
            .staleness_of(self.get_item_input_box()))
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_error_messages_are_cleared_on_input(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertTrue(error.is_displayed())

        self.get_item_input_box().send_keys('a')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertFalse(error.is_displayed())
