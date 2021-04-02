import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class CES_ATS_LOGIN(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ces(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://localhost:8080")
        #driver.get("https://ces.herokuapp.com/")
        time.sleep(3)
        elem = driver.find_element_by_link_text("Log in").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/div/div[2]/div/div/div/form/div[1]/div/input")
        elem.send_keys("advisor")
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/div/div[2]/div/div/div/form/div[2]/div/input")
        elem.send_keys("instagram")
        time.sleep(3)
        elem= driver.find_element_by_xpath("/html/body/div/div[3]/div/div/div/div[2]/div/div/div/button").click()
        time.sleep(3)
        try:
           # elem= driver.find_element_by_xpath("/html/body/div/div[3]/div/p") #verifies successful login using xpath to (div class)message "Hello.."
            time.sleep(3)

            elem = driver.find_element_by_link_text("Contact Us")
            elem = driver.find_element_by_link_text("Contact Us").click()
            #elem = driver.find_element_by_tag_name('h3') -- change this to a tag on contact us page
            time.sleep(3)

            #code for logout
            # click on username on the right side of screen
            elem = driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[3]/div/button").click()
            time.sleep(3)
            # select dropdown for logout
            elem= driver.find_element_by_link_text("Log out").click()
            #elem= driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[3]/div/ul/li/a").click()

            #verify if we are on home page
            #elem= driver.find_element_by_xpath("/html/body/div/div[3]/div/p") #verifies successful logout using xpath
            time.sleep(3)
            assert True

        except NoSuchElementException:
            self.fail("Login failed")
            assert False

        time.sleep(3)


def tearDown(self):
    #self.driver.close()
    self.driver.quit()


if __name__ == '__main__':
    unittest.main()