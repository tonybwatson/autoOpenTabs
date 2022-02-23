from selenium import webdriver
import webbrowser
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(ChromeDriverManager().install())

# Change URL in browser.get to the address of the page you want to open links on
browser.get('https://findhelpnowky.org/ky')



# Give the computer a few seconds to load the page
time.sleep(5)

# Get the "a" tags
elem = browser.find_elements_by_tag_name("a")

# And open the tags, unless they are None, are phone numbers, or scroll to a main-content anchor tag on the page
for link in elem:
    linkHref = link.get_attribute("href")
    if linkHref == None or "tel:" in linkHref or "#main-content" in linkHref:
        pass
    else:
        if "http" in linkHref:
            # print(linkHref)
            webbrowser.open_new_tab(linkHref)

time.sleep(10)

browser.close()