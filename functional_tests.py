from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.http import HttpRequest
from lists.views import home_page

import unittest


class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retreive_it_later(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows),
        	"New to-do item did not appear in table"
		)
		self.fail('Finish the tests!')

	def test_home_page_can_save_a_POST_request(self):
	    request = HttpRequest()
	    request.method = 'POST'
	    request.POST['item_text'] = 'A new list item'

	    response = home_page(request)

	    self.assertIn('A new list item', response.content.decode())


if __name__ == '__main__':
	unittest.main(warnings='ignore')