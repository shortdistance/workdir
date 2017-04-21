#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url1 = "http://172.21.0.33:11001"
username1 = 'fadq01'
password1= '111111'

def login (url, username, password):
    browser = webdriver.Ie()
    browser.get(url)
    browser.maximize_window()

    username_textctl = browser.find_element_by_id("login_no")
    password_textctl = browser.find_element_by_id("login_password")
    username_textctl.send_keys(username)
    password_textctl.send_keys(password)
    print browser.current_url
    
    browser.find_element_by_name("btn1").submit()
    
    #browser.implicitly_wait(30)
    print browser.current_url
    
    #print browser.window_handles
    #print browser.switch_to().window
    
if __name__ == '__main__':
    login(url1, username1, password1)
    