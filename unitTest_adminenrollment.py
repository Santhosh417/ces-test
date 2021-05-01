import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class CES_ATS_ADMINENROLLMENT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ces(self):
        driver = self.driver
        driver.maximize_window()
        #driver.get("http://127.0.0.1:8000/popcorn/")
        driver.get("https://ces-service.herokuapp.com/popcorn/")
        time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("admin")
        time.sleep(2)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("admin")
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        try:
            elem= driver.find_element_by_xpath("/html/body/div/div[2]/h1") #site administration
            time.sleep(2)
            elem=driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[1]/a").click() #add enrollment
            elem=driver.find_element_by_xpath("/html/body/div[1]/div[3]/h1") #ensure browser is on 'add enrollment' page

            #add enrollment details
            # add course
            elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[1]/div/div/select/option[2]").click()
            time.sleep(1)
            # add student
            elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[2]/div/div/select/option[2]").click()
            time.sleep(1)
            # id_semester_name
            elem = driver.find_element_by_id("id_semester_name")
            elem.send_keys("Summer 2021")
            time.sleep(2)
            # start and end date
            #select calendar
            elem = driver.find_element_by_id("id_start_date").clear()
            elem = driver.find_element_by_id("id_start_date")
            elem.send_keys("2021-05-17")
            #elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[4]/div/span[1]/a[2]/span").click()
            #elem = driver.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr[5]/td[2]/a").click()
            time.sleep(2)
            # select calendar
            elem = driver.find_element_by_id("id_end_date").clear()
            elem = driver.find_element_by_id("id_end_date")
            elem.send_keys("2021-08-13")
            #elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[5]/div/span[1]/a[2]/span").click()
            #elem= driver.find_element_by_xpath("/html/body/div[3]/div[2]/table/tbody/tr[4]/td[6]/a").click()

            time.sleep(2)
            # id_status
            elem = driver.find_element_by_id("id_status")
            elem.send_keys("Planned")
            time.sleep(2)
            #save enrollment
            elem= driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
            time.sleep(3)

            #delete - Deletes the first enrollment on the list
            elem=driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a").click()
            time.sleep(3)
            elem=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/p/a").click()
            #confirmation page- click on yes i am sure
            elem = driver.find_element_by_xpath("/html/body/div/div[3]/h1")
            time.sleep(1)
            elem=driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[2]").click()
            time.sleep(3)

            assert True

        except NoSuchElementException:
            self.fail("Add failed")
            assert False

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == '__main__':
    unittest.main()
