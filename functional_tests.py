#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 用户查看应用首页
        self.browser.get('http://localhost:8000')

        # 用户注意到网页标题和头部都包含了"To-Do"这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请用户输入一个代办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 用户在文本框输入了'Buy peacock feathers'
        inputbox.send_keys('Buy peacock feathers')

        # 按回车键后，页面更新了
        # 代办事项表格中显示了'1: Buy peacock feathers'
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        # 页面又显示了一个文本框，可以输入其他的代办事项
        # 用户输入了"Use peacock feathers to make a fly"
        self.fail('Finish the test!')

        # 页面再次更新，清单中显示了这两个代码事项

if __name__ == '__main__':
    unittest.main()
