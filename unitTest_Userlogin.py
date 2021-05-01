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
        #driver.get("http://localhost:8081")
        driver.get("https://jolly-shockley-7553c8.netlify.app/")
        time.sleep(5)
        elem = driver.find_element_by_link_text("Login").click()
        time.sleep(3)
        elem=  driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/div/form/div[1]/div/input")
        elem.send_keys("admin")
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/div/form/div[2]/div/input")
        elem.send_keys("admin")
        time.sleep(3)
        elem= driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/div/button").click()
        time.sleep(3)
        try:
            elem= driver.find_element_by_link_text("Search") #verifies successful login using link text for search button
            time.sleep(3)

            elem = driver.find_element_by_link_text("About us")
            elem = driver.find_element_by_link_text("About us").click()
            elem = driver.find_element_by_tag_name('h3')
            time.sleep(3)
            elem = driver.find_element_by_link_text("Alumni")
            elem = driver.find_element_by_link_text("Alumni").click()
            elem = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/h1/b')
            time.sleep(3)
            elem = driver.find_element_by_link_text("Contact Us")
            elem = driver.find_element_by_link_text("Contact Us").click()
            elem = driver.find_element_by_xpath('/html/body/div/div[2]/h6')
            time.sleep(3)

            #code for logout
            # click on username on the right side of screen
            elem = driver.find_element_by_xpath("/html/body/div/div[1]/div/div[3]/div/button").click()

            time.sleep(3)
            # select dropdown for logout
            elem= driver.find_element_by_link_text("Log out").click()
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