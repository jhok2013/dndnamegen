import unittest 
import sys
from pathlib import Path

sys.path.insert(0, '..')

from dndnamegen.NameGenAPI import NameGenAPI #type: ignore

# C:\Program Files (x86)\Google\Chrome\Application

class test_dndnamegen(unittest.TestCase):
    '''
    Handles all the tests for the NameGenAPI.
    '''
    wsl_path: Path = Path('../bin/chromedriver-linux64')
    win_path: str = "C:\Program Files (x86)\chromedriver.exe"
    win_bin_path: str = "..\\bin\chromedriver.exe"
    
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_win_path(self) -> None:
        '''
        Tests whether the NameGenAPI can run with the default
        location of the chromedriver.exe on windows.
        '''
        try:
            name_gen_api: NameGenAPI = NameGenAPI(binary_path=self.win_path)
            name_gen_api.generate_names()
            self.assertTrue(True, "Test: test_win_path has passed.")
        except Exception as e:
            print(e)
            self.fail("Failure: test_win_path has failed.")
    
    def test_win_bin(self) -> None:
        '''
        Tests whether the chromedriver.exe runs can run in the
        built-in bin folder of the program.
        '''
        try:
            name_gen_api: NameGenAPI = NameGenAPI(binary_path=self.win_bin_path)
            name_gen_api.generate_names()
            self.assertTrue(True, "Test: test_win_bin has passed.")
        except Exception as e:
            print(e)
            self.fail("Failure: test_win_bin has failed.")

if __name__ == "__main__":
    unittest.main()