import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class CES_ATS_ADDENROLL(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ces(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://localhost:8081")
        #driver.get("https://jolly-shockley-7553c8.netlify.app/")
        #time.sleep(5)
        elem = driver.find_element_by_link_text("Login").click()
        #time.sleep(3)
        elem=  driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/div/form/div[1]/div/input")
        elem.send_keys("admin")
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/div/form/div[2]/div/input")
        elem.send_keys("instagram")
        time.sleep(3)
        elem= driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/div/button").click()
        time.sleep(3)
        try:
            elem= driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div[2]/div[1]/div/input")
            elem.send_keys("12345")
            time.sleep(3)
            #click on search
            elem= driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div[2]/div[2]/a").click()
            time.sleep(3)

            #click on add course to study plan
            elem = driver.find_element_by_link_text("Add a course to study plan")
            elem= driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/a").click()

            #add course
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div/div[1]/div[2]").click()
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div/div[1]/div[3]/ul/li[1]/span").click()
            time.sleep(2)
            # start date
            elem= driver.find_element_by_id('start-date')
            elem =driver.find_element_by_xpath("/html/body/div/div[2]/div[4]/div[1]/div/div/div[1]/label").click()
            #select date
            time.sleep(2)
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[4]/div[1]/div/div/div[1]/div/div/div/div[2]/div[2]/div[4]/div[3]/span").click()
            #end date
            elem = driver.find_element_by_id('end-date')
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[4]/div[2]/div/div/div[1]/label").click()
            #select date
            time.sleep(2)
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[4]/div[2]/div/div/div[1]/div/div/div/div[2]/div[2]/div[5]/div[6]/span").click()
            time.sleep(3)

            #select semester
            elem= driver.find_element_by_xpath("/html/body/div/div[2]/div[5]/div/div/div/div[1]/div[2]/span").click()
            elem= driver.find_element_by_xpath("/html/body/div/div[2]/div[5]/div/div/div/div[1]/div[3]/ul/li[4]/span/span").click()
            #enroll
            elem=driver.find_element_by_xpath("/html/body/div/div[2]/div[6]/div/div/button[1]").click()
            time.sleep(2)

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
            self.fail("Add failed or course does not exist")
            assert False

        time.sleep(3)


def tearDown(self):
    #self.driver.close()
    self.driver.quit()


if __name__ == '__main__':
    unittest.main()