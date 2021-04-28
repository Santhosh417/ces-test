import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class CES_ATS_EDITENROLL(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ces(self):
        driver = self.driver
        driver.maximize_window()
        # driver.get("http://localhost:8081")
        driver.get("https://jolly-shockley-7553c8.netlify.app/")
        time.sleep(5)
        elem = driver.find_element_by_link_text("Login").click()
        #time.sleep(3)
        elem=  driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/div/form/div[1]/div/input")
        elem.send_keys("instructor")
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/div/form/div[2]/div/input")
        elem.send_keys("gounomavs1a")
        time.sleep(3)
        elem= driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/div/button").click()
        time.sleep(3)
        try:
            elem= driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div[2]/div[1]/div/input")
            elem.send_keys("11565601")
            time.sleep(3)
            #click on search
            elem= driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div[2]/div[2]/a").click()
            time.sleep(3)
            #Ensure enrollment page
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]/div/table/caption/p")

            #edit
            # Locate edit button
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[7]/button[1]").click()
            time.sleep(3)

            #Update the changes
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/div/div/div/input").clear()
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/div/div/div/input")
            elem.send_keys("Fall 2022")
            time.sleep(3)

            #Save changes
            # Submit the edit
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[4]/div/button").click()
            time.sleep(3)
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]/div/table/caption/p")


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
            self.fail("Edit failed or entry does not exist")
            assert False

        time.sleep(3)


def tearDown(self):
    #self.driver.close()
    self.driver.quit()


if __name__ == '__main__':
    unittest.main()