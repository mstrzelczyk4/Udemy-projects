import unittest
from tests.test_ContactFormTest import ContactFormTest
from tests.test_EnterTextTest import EnterTextTest


cf = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)
et = unittest.TestLoader().loadTestsFromTestCase(EnterTextTest)

regressionTest = unittest.TestSuite([cf, et])

unittest.TextTestRunner(verbosity=1).run(regressionTest)

