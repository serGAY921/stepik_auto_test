from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

    time.sleep(1)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
