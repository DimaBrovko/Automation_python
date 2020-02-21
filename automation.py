from selenium import webdriver

crhome_browser = webdriver.Chrome('./chromedriver')

crhome_browser.maximize_window()

crhome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy' in crhome_browser.title
shwon_message_button = crhome_browser.find_element_by_class_name('btn.btn-default')
#print(shwon_message_button.get_attribute('innerHTML'))

assert 'Show Message' in crhome_browser.page_source

user_message = crhome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('123')

shwon_message_button.click()
output_message = crhome_browser.find_element_by_id('display')

assert '123' in output_message.text

crhome_browser.close()
crhome_browser.quit()