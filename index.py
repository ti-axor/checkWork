from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

# credentials
username = os.getenv("USER")
password = os.getenv("PASSWORD")


def access_site_by_chrome(site):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless=new")
    # # chrome_options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(options=chrome_options)
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(site)
    # input de keys
    driver.find_element("id", "btnMarcarPonto").click()
    driver.find_element(
        "id",
        "LogOnModel_UserName_Marcacao"
        ).send_keys(username)
    driver.find_element(
        "id",
        "LogOnModel_Password_Marcacao"
        ).send_keys(password)
    driver.find_element("id", "btnSubmitMarcacao").click()


if __name__ == "__main__":
    try:
        today = datetime.today().strftime("%d-%m-%Y %H:%M:%S")
        # acessar site
        access_site_by_chrome("https://www.mdcomune.com.br/")
        with open("log.txt", "a") as log:
            log.write(f"{today}: ok\n")
            print(f"{today}: ok")
            log.close()
    except WebDriverException as e:
        with open("log.txt", "a") as log:
            log.write(f"{today}: {e.msg}")
            print(f"{today}: {e.msg}")
            log.close()
