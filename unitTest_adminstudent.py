import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class CES_ATS_STUDENT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ces(self):
        driver = self.driver
        driver.maximize_window()
        #driver.get("http://127.0.0.1:8000/admin")
        driver.get("https://ces-service.herokuapp.com/admin/")
        time.sleep(5)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("admin")
        time.sleep(2)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("instagram")
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        try:
            elem= driver.find_element_by_xpath("/html/body/div/div[2]/h1") #site administration
            time.sleep(2)
            elem=driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[3]/table/tbody/tr[3]/td[1]/a").click() #add student
            elem = driver.find_element_by_xpath("/html/body/div/div[3]/h1")  # ensure browser is on 'add student' page

            # add student details
            # id_name
            elem = driver.find_element_by_id("id_name")
            elem.send_keys("Automate Test1")
            time.sleep(2)
            # id_nuid
            elem = driver.find_element_by_id("id_nuid")
            elem.send_keys("987654")
            time.sleep(2)
            # id_email
            elem = driver.find_element_by_id("id_email")
            elem.send_keys("atstest@gmail.com")
            time.sleep(2)
            # id_cell_phone
            elem = driver.find_element_by_id("id_cell_phone")
            elem.send_keys("4000011234")
            time.sleep(2)
            # id_start_date
            elem = driver.find_element_by_id("id_start_date").clear()
            elem = driver.find_element_by_id("id_start_date")
            elem.send_keys("2021-05-17")
            time.sleep(2)
            # id_graduation_date
            elem = driver.find_element_by_id("id_graduation_date").clear()
            elem = driver.find_element_by_id("id_graduation_date")
            elem.send_keys("2023-12-20")
            time.sleep(2)
            # save student
            elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
            time.sleep(3)

            # delete
            elem = driver.find_element_by_link_text("Automate Test1").click()
            time.sleep(3)
            elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/p/a").click() # delete student
            # confirmation page- click on yes i am sure
            elem = driver.find_element_by_xpath("/html/body/div/div[3]/h1") # ensure the delete confirmation page
            time.sleep(1)
            elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[2]").click() # Confirm to delete the student
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