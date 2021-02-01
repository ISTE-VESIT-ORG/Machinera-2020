from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from shutil import which

# Selenium Code
chrome_path = which("chromedriver")
driver = webdriver.Chrome(executable_path=chrome_path)
driver.get("https://web.whatsapp.com/")

# Scan QR Code
input("Scan the QR Code and press any key.")
print("Key entered")
time.sleep(3)

# Search input
search_input = driver.find_element_by_xpath("(//span[@title='Srajan Vesit IT'])")
search_input.click()

# Send Message
message = "Spam Message"
message_input = driver.find_element_by_xpath("(//*[@id='main']/footer/div[1]/div[2]/div/div[2])")
message_input.send_keys(message)
message_input.send_keys(Keys.ENTER)


# Close Driver
time.sleep(5)
driver.close()