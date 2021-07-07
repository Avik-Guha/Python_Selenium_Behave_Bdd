import inspect
import logging
import time

from selenium import webdriver
# from selenium.webdriver import Chrome, Firefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager


def start_browser_driver(browser):
    global driver

    if str(browser) == "Chrome":
        # chrome_driver_path = "Driver\\chromedriver.exe"
        # driver = Chrome(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif str(browser) == "ChromeHeadless":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    elif str(browser) == "Firefox":
        # firefox_driver_path = "Driver\\geckodriver.exe"
        # driver = Firefox(executable_path=firefox_driver_path)
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif str(browser) == "IE":
        driver = webdriver.Ie(IEDriverManager().install())
    elif str(browser) == "Edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # chrome_driver_path = "Driver\\chromedriver.exe"
        # driver = Chrome(executable_path=chrome_driver_path)

    driver.delete_all_cookies()
    driver.maximize_window()


def set_env(environment):
    global Base_Url

    if str(environment) == "QA":
        Base_Url = "https://www.thetestingworld.com/testings/"
    elif str(environment) == "PROD":
        Base_Url = "https://www.thetestingworld.com/testings/PROD"
    else:
        Base_Url = "https://www.thetestingworld.com/testings/"


def set_logger():
    global logger
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    handler_info = logging.FileHandler('Logs/info_log.txt')
    handler_info.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler_info.setFormatter(formatter)
    logger.addHandler(handler_info)

    return logger


def set_driver(browser):
    start_browser_driver(browser)


def get_driver():
    return driver


def set_environment(environment):
    set_env(environment)


def get_environment():
    return Base_Url


def close_browser():
    driver.quit()


def wait_for_seconds(seconds):
    time.sleep(seconds)
