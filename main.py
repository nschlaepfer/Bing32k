from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Navigate to the URL
        url = 'https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx'
        driver.get(url)

        # Select the 'Creative' option
        creative_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Creative") and contains(@class, "label")]'))
        )
        creative_label.click()

        # Modify the textarea's maxlength attribute from 2000 to 100000
        textarea = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//textarea[contains(@class, "text-area") and @id="searchbox" and @name="searchbox"]'))
        )
        driver.execute_script("arguments[0].setAttribute('maxlength', '100000')", textarea)

        # Add your interactions with the website here
        time.sleep(10)  # Pause for 10 seconds to see the changes

    finally:
        driver.quit()

if __name__ == '__main__':
    main()
