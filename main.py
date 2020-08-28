from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import Chrome


browser = webdriver.Chrome('C:\driver\chromedriver.exe')
browser.implicitly_wait(2)

browser.get("https://mycas.sta.uwi.edu/cas/login?service=https%3A%2F%2Fssb2.sta.uwi.edu%2Fproddad%2Ftwzkcasl.P_Service_Ticket%3Ftarget%3Dbwsksmrk.p_write_term_selection")

username_input = browser.find_element_by_id('username')
pwd_input = browser.find_element_by_id('password')

username_input.send_keys('816003022')
pwd_input.send_keys('K5D5#4c3')

login_button = browser.find_element_by_name('submit')
login_button.click()

submit_term_button = browser.find_element_by_xpath("//input[@value='Submit']")
submit_term_button.click()

course_code_link = browser.find_element_by_xpath("//*[contains(text(), '28457')]")
course_code_link.click()

sleep(5)