from unittest import TestLoader, TextTestRunner, TestSuite
#import tests.unitTest_Navigation
from tests.unitTest_Userlogin import CES_ATS_LOGIN
from tests.unitTest_search import CES_ATS_SEARCH
from tests.unitTest_addenrollment import CES_ATS_ADDENROLL
from tests.unitTest_deleteenrollment import CES_ATS_DELETEENROLL
#test for edit
from tests.unitTest_adminenrollment import CES_ATS_ADMINENROLLMENT
from tests.unitTest_admincourse import CES_ATS_COURSE
from tests.unitTest_adminstudent import CES_ATS_STUDENT


if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((

        loader.loadTestsFromTestCase(CES_ATS_LOGIN),
        loader.loadTestsFromTestCase(CES_ATS_SEARCH), #includes download plan as well
        loader.loadTestsFromTestCase(CES_ATS_ADDENROLL),
        loader.loadTestsFromTestCase(CES_ATS_DELETEENROLL),
        #edit goes here
        loader.loadTestsFromTestCase(CES_ATS_ADMINENROLLMENT),
        loader.loadTestsFromTestCase(CES_ATS_COURSE),
        loader.loadTestsFromTestCase(CES_ATS_STUDENT)

    ))
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

