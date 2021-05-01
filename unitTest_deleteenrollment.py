import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException


class CES_ATS_DELETEENROLL(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ces(self):
        driver = self.driver
        driver.maximize_window()
        #driver.get("http://localhost:8081")
        driver.get("https://jolly-shockley-7553c8.netlify.app/")
        time.sleep(3)
        elem = driver.find_element_by_link_text("Login").click()
        #time.sleep(3)
        elem=  driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/div/form/div[1]/div/input")
        elem.send_keys("admin")
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/div/form/div[2]/div/input")
        elem.send_keys("admin")
        time.sleep(3)
        elem= driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/div/button").click()
        time.sleep(3)
        try:
            elem= driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div[2]/div[1]/div/input")
            elem.send_keys("27867799")
            time.sleep(3)
            #click on search
            elem= driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div[2]/div[2]/a").click()
            time.sleep(3)

            #click on delete for a course
            # old elem =driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/table/tbody/tr[3]/td[7]/button[2]").click()
            elem =driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[7]/button[2]").click()
            #elem = driver.find_element_by_link_text("Delete")
            #elem = driver.find_element_by_link_text("Delete").click()
            time.sleep(2)
            obj = driver.switch_to.alert
            time.sleep(3)
            obj.accept()
            time.sleep(3)

            #code for logout
            # click on username on the right side of screen
            elem = driver.find_element_by_xpath("/html/body/div/div[1]/div/div[3]/div/button").click()

            time.sleep(3)
            # select dropdown for logout
            elem= driver.find_element_by_link_text("Log out").click()
            #elem= driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[3]/div/ul/li/a").click()
            time.sleep(3)
            assert True

        except NoSuchElementException:
            self.fail("delete failed or course does not exist")
            assert False

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == '__main__':
    unittest.main()
