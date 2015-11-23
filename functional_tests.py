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
        self.assertIn('1: Buy peacock feathers',[row.text for row in rows])

        # 页面又显示了一个文本框，可以输入其他的代办事项
        # 用户输入了"Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # 页面再次更新，清单中显示了这两个代码事项
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers',[row.text for row in rows])
        self.assertIn(
            '2: Use peacock feathers to make a fly',
            [row.text for row in rows]
        )

        # 用户想知道网站是否记住他的清单
        # 用户看到网站为他生成了唯一的URL
        # 页面中有一些文字解说这个功能
        self.fail('Finish the test!')

        # 用户访问了那个URL，发现办事项清单还在

if __name__ == '__main__':
    unittest.main()
