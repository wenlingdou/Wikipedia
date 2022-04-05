# 1. Using Selenium WebDriver, open the web browser.
# 2. Maximize the browser window.
# 3. Navigate to https://en.wikipedia.org/ (Links to an external site.) web URL
# 4. Check URL and title are as expected.
# 5. In a search field, find searchInput and click on it.
# 6. Check that the title Python (programming language) is displayed.
# 7. Click by the Wikipedia main image (logo) to navigate back to the home page and close the browser.

import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)

app = 'wikipedia'
wiki_url = 'https://en.wikipedia.org/wiki/Main_Page'
wiki_homepage_title = 'Wikipedia, the free encyclopedia'
wiki_navigation_url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
wiki_navagation_title = 'Python (programming language) - Wikipedia'

def setUp():
    print(f'Launch {app} App')
    print(f'--------------------------------------------------')

    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(wiki_url)
    if driver.current_url == wiki_url and driver.title == wiki_homepage_title:
        print(f'Welcome to {app}! {app} App website launched successfully!')
        print(f'{app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Homepage title: {driver.title}')
        tearDown()

def tearDown():
    if driver is not None:
        print('--------------------------------------------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()

def navigation():
    if driver.current_url == wiki_url:
        driver.find_element(By.ID, 'searchInput').click()
        driver.find_element(By.ID, 'searchInput').clear()
        driver.find_element(By.ID, 'searchInput').send_keys('Py')
        sleep(0.5)
        driver.find_element(By.LINK_TEXT, 'Python (programming language)').click()
        sleep(0.5)


        if driver.current_url == wiki_navigation_url and driver.title == wiki_navagation_title:
            print(f'{app} Python programming page URL: {wiki_navigation_url}, page title: {wiki_navagation_title}')
            print(f'{app} Python programming page is displayed successfully!')
            sleep(0.5)

            driver.find_element(By.ID, 'p-logo').click()
            print('------------Click the logo, then go back to home page.')
            sleep(0.25)
        else:
            print(f'Python programming page is not displayed. Please check your code.')


setUp()
navigation()
tearDown()

