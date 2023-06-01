from pprint import pprint
import time
import re
import csv

from selenium.webdriver.common.keys import Keys
from selenium_scrapper import get_data
from selenium_driver import selenium_driver

driver = selenium_driver()

config = {
    "user": {
        "email": "zaptom.pro@gmail.com",
        "password": "Tom01032000",
        "phone": "066577418"
    },
}
data = []
while not driver.is_attached('body > .application-outlet *'):
    driver.get('https://linkedin.com')
    if driver.is_attached('#session_key'):
        driver.write('#session_key', config['user']['email'])
        driver.write('#session_password', config['user']['password'])
        driver.click('[data-id="sign-in-form__footer"] button')
        time.sleep(3)
    time.sleep(2)
    driver.captcha()
print('logged in !')
driver.get(
    f"https://www.linkedin.com/jobs/search/?keywords=communication&location=Clichy%2C%20%C3%8Ele-de-France%2C%20France&refresh=true&sortBy=R")

data.extend(get_data(driver=driver))

# config = {
#     "user": {
#         "email": "t.zapico@ldeclic.fr",
#         "password": "Tom01032000",
#         "phone": "066577418"
#     },
# }
# while not driver.is_attached('#container > #app-root *'):
#     driver.get('https://secure.indeed.com')
#     # EMAIL
#     driver.write('#emailform input', config['user']['email'])
#     driver.write('#emailform input', Keys.ENTER)
#     if driver.is_attached('#emailform'):
#         driver.write('#emailform input', config['user']['email'])
#     while not driver.is_attached('#loginform'):
#         time.sleep(1)
#     driver.click('#onetrust-accept-btn-handler')
#     # PASSWORD
#     driver.write('#loginform input[type="password"]',
#                  config['user']['password'])
#     driver.write('#loginform input[type="password"]', Keys.ENTER)
#     if driver.is_attached('#loginform'):
#         driver.write('#loginform input[type="password"]',
#                      config['user']['password'])
#     while not driver.is_attached('#two-factor-auth-form'):
#         time.sleep(1)
#     # PHONE
#     while driver.is_attached('#two-factor-auth-form'):
#         time.sleep(1)
# print('logged in !')
# driver.get(
#     f"https://fr.indeed.com/jobs?q=marketing&l=Clichy+%2892%29")

pprint(data)
print('creating csv')
if len(data) > 0:
    with open('D:\\PythonPackages\\selenium_scrapper\\scrapping\\linkedin_jobs3.csv', 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = list(data[0])
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            for prop in item:
                item[prop] = item[prop]
            writer.writerow(item)

time.sleep(9999)