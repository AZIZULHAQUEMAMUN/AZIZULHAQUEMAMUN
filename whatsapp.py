from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Launch Chrome (ensure chromedriver is installed and in PATH)
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)  # wait for QR code scan

# Replace with your friend's name or group name
target = "Friend's Name"

# Message to send
message = "Message sent using Python!!!"

# Locate chat by title
x_arg = f'//span[@title="{target}"]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()

# Locate message input box (more stable locator)
inp_xpath = '//div[@aria-label="Type a message"]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

# Send message a few times
for i in range(5):  # safer than 100
    input_box.send_keys(message + Keys.ENTER)
    time.sleep(1)

print("Messages sent successfully!")
driver.quit()
