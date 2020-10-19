import unittest 
import sys
from pathlib import Path

sys.path.insert(0, '..')

from dndnamegen.NameGenAPI import NameGenAPI #type: ignore

# C:\Program Files (x86)\Google\Chrome\Application

class test_dndnamegen(unittest.TestCase):
    '''

    '''
    wsl_path: Path = Path('../bin/chromedriver-linux64')
    #win_path: str = "C:\Program Files (x86)\chromedriver.exe"
    win_path: str = r"C:\projects\dndnamegen\bin\chromedriver.exe"
    
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_get_names(self) -> None:
        '''

        '''
        name_gen_api: NameGenAPI = NameGenAPI(binary_path=self.win_path)
        name_gen_api.generate_names()

if __name__ == "__main__":
    unittest.main()