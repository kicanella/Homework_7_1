from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selene import browser
# Открываем браузер
browser.config.hold_driver_at_exit = True  # оставить браузер открытым
browser.open('https://qa.guru/cms/system/login')


