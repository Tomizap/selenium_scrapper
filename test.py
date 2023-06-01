from selenium_driver import selenium_driver

driver = selenium_driver()

url = "https://google.com"
driver.execute_script(f"window.open('{url}')")
window_handles = driver.window_handles()
print(window_handles)
print(len(driver.window_handles()))

driver.switch_to_window(window_handles[1])
