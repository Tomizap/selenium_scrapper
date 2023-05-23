from pprint import pprint
from selenium_scrapper import selenium_scrapper
from selenium_driver import selenium_driver

data = selenium_scrapper(driver=selenium_scrapper(), url=f"https://www.linkedin.com/jobs/search/?currentJobId=3612871351&geoId=103029567&keywords=marketing&location=Clichy%2C%20%C3%8Ele-de-France%2C%20France&refresh=true")
pprint(data)
