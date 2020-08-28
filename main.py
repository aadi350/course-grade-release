from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

print('Enter ID')
username = input()
print('Enter password')
pwd = input()

options = Options()
options.binary_location = 'D:\Program Files\Google\Chrome\Application\chrome.exe'
browser = webdriver.Chrome(executable_path=r'D:\chromedriver\chromedriver.exe', options=options)
browser.implicitly_wait(2)

browser.get("https://mycas.sta.uwi.edu/cas/login?service=https%3A%2F%2Fssb2.sta.uwi.edu%2Fproddad%2Ftwzkcasl.P_Service_Ticket%3Ftarget%3Dbwsksmrk.p_write_term_selection")

username_input = browser.find_element_by_id('username')
pwd_input = browser.find_element_by_id('password')



username_input.send_keys(username)
pwd_input.send_keys(pwd)

login_button = browser.find_element_by_name('submit')
login_button.click()

submit_term_button = browser.find_element_by_xpath("//input[@value='Submit']")
submit_term_button.click()

course_code_link = browser.find_element_by_xpath("//*[contains(text(), '28457')]")
course_code_link.click()

course_info = browser.find_elements_by_class_name('ntdefault')
course_info_labels = browser.find_elements_by_class_name('ntlabel')

for info, labels in zip(course_info, course_info_labels):
    print('{} {}'.format(labels.text, info.text))

sleep(5)
