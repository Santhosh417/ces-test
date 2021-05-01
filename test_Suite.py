from unittest import TestLoader, TextTestRunner, TestSuite
from tests.unitTest_Userlogin import CES_ATS_LOGIN
from tests.unitTest_search import CES_ATS_SEARCH
from tests.unitTest_addenrollment import CES_ATS_ADDENROLL
from tests.unitTest_deleteenrollment import CES_ATS_DELETEENROLL
from tests.unitTest_editenrollment import CES_ATS_EDITENROLL
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
        loader.loadTestsFromTestCase(CES_ATS_EDITENROLL),
        loader.loadTestsFromTestCase(CES_ATS_ADMINENROLLMENT),
        loader.loadTestsFromTestCase(CES_ATS_COURSE),
        loader.loadTestsFromTestCase(CES_ATS_STUDENT),

    ))
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

