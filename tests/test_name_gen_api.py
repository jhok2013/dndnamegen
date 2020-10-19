import unittest
import sys

sys.path.insert(0, '..')

from dndnamegen.name_gen_api import name_gen_api

class test_dndnamegen(unittest.TestCase):
    '''

    '''
    name_gen_api: name_gen_api = name_gen_api()
    
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_get_names(self) -> None:
        '''

        '''
        self.name_gen_api.get_names(race_name='aasimar', source='default')

if __name__ == "__main__":
    unittest.main()