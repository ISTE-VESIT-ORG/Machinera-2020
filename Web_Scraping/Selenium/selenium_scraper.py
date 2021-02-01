from selenium import webdriver
from shutil import which

chrome_path = which("chromedriver")

driver = webdriver.Chrome(executable_path=chrome_path)
driver.get("https://duckduckgo.com")

# Find Element by ID/Tag/Class_Name/Xpath/CSS_Selector
search_input = driver.find_element_by_id("search_form_input_homepage")

'''
driver.find_element_by_class_name(name)
driver.find_element_by_xpath(xpath)
driver.find_element_by_css_selector(css_selector)
driver.find_element_by_tag_name("h1")

# Multiple elements
driver.find_elements_by_class_name()
'''

# Automate - Input on Search Engine
search_input.send_keys("ISTE-VESIT")

# Click on button
search_btn = driver.find_element_by_id("search_button_homepage")
search_btn.click()

'''search_input.send_keys(Keys.ENTER)'''

# Scraping
results = driver.find_elements_by_xpath("(//a[@class='result__a'])")
for result in results:
    print(result.text)


# print(driver.page_source)
driver.close()
