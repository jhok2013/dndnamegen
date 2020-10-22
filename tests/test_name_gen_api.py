# Standard library imports
import unittest 
import sys
from pathlib import Path
from typing import List

p: str = "C:\projects"
sys.path.insert(0, p)

from dndnamegen.namegen.NameGenAPI import NameGenAPI #type: ignore
class test_dndnamegen(unittest.TestCase):
    '''
    Handles all the tests for the NameGenAPI.
    '''
    wsl_path: Path = Path('../bin/chromedriver-linux64')
    win_path: str = "C:\Program Files (x86)\chromedriver.exe"
    win_bin_path: str = "C:\projects\dndnamegen\\bin\chromedriver.exe"
    
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    @unittest.skip('Reason: Redundant test')
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
    
    @unittest.skip('Reason: Redundant test')
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
    
    def test_multiple_genders(self) -> None:
        '''

        '''
        names: List[str] = []
        name_amount: int
        return_amount: int
        try:
            name_gen_api: NameGenAPI = NameGenAPI(binary_path=self.win_bin_path)
            names = name_gen_api.generate_names(race_name='aasimar', gender=['male', 'female'])
            name_amount = 20
            return_amount = len(names)
            self.assertEqual(
                first=name_amount,
                second=return_amount,
                msg='Test: test_multiple_genders has succeeded.'
            )
        except Exception as e:
            print(e)
            self.fail("Failure: test_multiple_genders has failed.") 

    def test_single_gender(self) -> None:
        '''

        '''
        names: List[str] = []
        name_amount: int
        return_amount: int
        try:
            name_gen_api: NameGenAPI = NameGenAPI(binary_path=self.win_bin_path)
            names = name_gen_api.generate_names(race_name='aasimar', gender=['male'])
            name_amount = 10
            return_amount = len(names)
            self.assertEqual(
                first=name_amount,
                second=return_amount,
                msg='Test: test_single_gender has succeeded.'
            )
        except Exception as e:
            print(e)
            self.fail("Failure: test_single_gender has failed.") 
    
    def test_single_gender_str(self) -> None:
        '''

        '''
        names: List[str] = []
        name_amount: int
        return_amount: int
        try:
            name_gen_api: NameGenAPI = NameGenAPI(binary_path=self.win_bin_path)
            names = name_gen_api.generate_names(race_name='aasimar', gender='male')
            name_amount = 10
            return_amount = len(names)
            self.assertEqual(
                first=name_amount,
                second=return_amount,
                msg='Test: test_single_gender_str has succeeded'
            )
        except Exception as e:
            print(e)
            self.fail("Failure: test_single_gender_str has failed.")
    
    def test_human_genders(self) -> None:
        '''

        '''
        names: List[str] = []
        name_amount: int
        return_amount: int
        try:
            name_gen_api: NameGenAPI = NameGenAPI(binary_path=self.win_bin_path)
            names = name_gen_api.generate_names(race_name='human', gender=['male', 'female', 'old male', 'old female'])
            name_amount = 64
            return_amount = len(names)
            self.assertEqual(
                first=name_amount,
                second=return_amount,
                msg='Test: Success'
            )
        except Exception as e:
            print(e)
            self.fail("Failure: test_win_bin has failed.")   

if __name__ == "__main__":
    unittest.main()