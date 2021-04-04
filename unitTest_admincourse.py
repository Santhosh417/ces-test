import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class CES_ATS_COURSE(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ces(self):
        driver = self.driver
        driver.maximize_window()
        #driver.get("http://localhost:8080")
        driver.get("https://ces-service.herokuapp.com/admin/")
        time.sleep(5)
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
            elem=driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/a").click() #add course
            elem=driver.find_element_by_xpath("/html/body/div/div[3]/h1") #ensure browser is on 'add course' page

            #add course details
            # id_coursename
            elem = driver.find_element_by_id("id_course_name")
            elem.send_keys("Selenium Course")
            time.sleep(2)
            # id_courseid
            elem = driver.find_element_by_id("id_course_id")
            elem.send_keys("ISQA Sel")
            time.sleep(2)
            # id_professor
            elem = driver.find_element_by_id("id_professor")
            elem.send_keys("Selenium")
            time.sleep(2)
            # id_program
            elem = driver.find_element_by_id("id_program")
            elem.send_keys("Graduate")
            time.sleep(2)
            # id_course_type
            elem = driver.find_element_by_id("id_course_type")
            elem.send_keys("On-line")
            time.sleep(2)
            # id_credits
            elem = driver.find_element_by_id("id_credits")
            elem.send_keys("3")
            time.sleep(2)
            #save course
            elem= driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/input[1]").click()
            time.sleep(3)

            #delete
            elem=driver.find_element_by_link_text("Selenium Course").click()
            time.sleep(3)
            elem=driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/p/a").click()
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
    #self.driver.close()
    self.driver.quit()


if __name__ == '__main__':
    unittest.main()