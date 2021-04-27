from unittest import TestLoader, TextTestRunner, TestSuite
#import tests.unitTest_Navigation
from tests.unitTest_Userlogin import CES_ATS_LOGIN
from tests.unitTest_search import CES_ATS_SEARCH
from tests.unitTest_addenrollment import CES_ATS_ADDENROLL
from tests.unitTest_deleteenrollment import CES_ATS_DELETEENROLL


if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((

        loader.loadTestsFromTestCase(CES_ATS_LOGIN),
        loader.loadTestsFromTestCase(CES_ATS_SEARCH),
        loader.loadTestsFromTestCase(CES_ATS_ADDENROLL),
        loader.loadTestsFromTestCase(CES_ATS_DELETEENROLL)

    ))
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

