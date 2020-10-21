'''
C:\Program Files (x86)\Google\Chrome\Application
'''
# Standard library imports
from json import loads 
from pathlib import Path
from typing import List, Any
from selenium import webdriver #type: ignore

#Third party imports
from selenium.webdriver.chrome.options import Options #type: ignore
from selenium.webdriver.common.by import By #type: ignore
from selenium.webdriver.support.ui import WebDriverWait #type: ignore
from selenium.webdriver.support import expected_conditions as EC #type: ignore

class NameGenAPI(object):
    '''
    
    '''
    race_name: str = 'Default'
    source: str = 'Default'
    _base_url: str = 'https://fantasynamegenerators.com/'
    name_amount: int = 1
    binary_path: str

    def __init__(self, race_name: str = 'Default', source: str = 'Default', 
                       name_amount: int = 1, binary_path: str = 'Default'):
        '''

        '''
        self.race_name = race_name
        self.source = source
        self.name_amount = name_amount
        self.binary_path = binary_path

    def generate_names(self, race_name: str = 'Default', 
                        source: str = 'Default', 
                        name_amount: int = 1) -> List[str]:
        '''
        TODO: Need to make it so that the scraper will find the div id=result tag
              Currently not able to find that tag 
              See line 63 - 64
        '''
        # Adjust self variables if needed
        self.race_name = race_name if race_name else self.race_name
        self.source = source if source else self.source
        self.name_amount = name_amount if name_amount else self.name_amount

        # Add return variable
        names: List[str] = []

        # Add options for chromedriver
        opts: Options = Options()
        opts.add_argument('--headless')
        opts.add_argument('--disable-gpu')
        race_url: str = self.__get_page(race_name=race_name)
        url: str = ''.join([self._base_url, race_url])

        # Get binary path from input
        binary_path: str = self.binary_path

        #Open browser and go to url
        browser: Any = webdriver.Chrome(executable_path=binary_path, options=opts) 
        browser.get(url=url)
        main = WebDriverWait(driver=browser, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="result"]'))
        )
        result_tag: str = main.find_element_by_xpath('//*[@id="result"]').text
        names = result_tag.splitlines()
        browser.quit()

        return names
    
    def __get_page(self, race_name: str) -> str:
        '''

        '''
        #path: Path = Path('.').resolve().joinpath('./data/name_generators.json')
        path: Path = Path('../data/name_generators.json').resolve()
        gen_dict: dict
        page: str = ''
        if page != 'Default':
            with open(path, 'r+') as f:
                gen_dict = loads(f.read())
                page = str(gen_dict.get(self.race_name))
        return page