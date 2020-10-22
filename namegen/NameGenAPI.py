# Standard library imports
from json import loads 
from pathlib import Path
from typing import List, Any, Dict, Union

#Third party imports
from selenium import webdriver #type: ignore
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
    gender: str

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
                        name_amount: int = 1) -> Union[List[str], str]:
        '''
        Returns the names for one or many races based on source, amount requested,
        race, and gender. Can use default values or if no input is given, will use
        random values.
        

        Parameters
        ----------
        race_name: str
            The name of the race used to generate names.
        source: str
            The Dungeons & Dragons 5e source book that provides the race.
        name_amount: int
            The amount of names to be returned.

        Returns
        -------
        names: Union[List[str], str]
            The names returned for the race. Can be one or multiple names. If
            one name is returned, then the type is string. Otherwise, the type is
            List[str]
        '''

        #- [] Add ability to call male or female names specifically.
        #- [x] Update name_generators.json to include gender information.
        #- [] Add packet ability to get names from multiple races and genders
        #  and return them as a json packet
        #- [] Add source filter to name_generator.json file

        # Adjust self variables if needed
        self.race_name = race_name if race_name else self.race_name
        self.source = source if source else self.source
        self.name_amount = name_amount if name_amount else self.name_amount

        # Add return variable
        names: Union[List[str], str] = []

        # Add options for chromedriver
        opts: Options = Options()
        opts.add_argument('--headless')
        opts.add_argument('--disable-gpu')
        race_packet: Dict[str, str] = self.__get_packet(race_name=race_name)
        race_url: str = race_packet[self.race_name]['generator'] #type: ignore
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
    
    def __get_packet(self, race_name: str) -> Dict[str, str]:
        '''
        Retrieves the data packet for a given race name, filter by race.
        TODO:
        - [] Add source filter to function so it can be filtered on function.
        - [] Add ability to filter on a default or without input.

        Parameters
        ----------
        race_name: str
            A name for the race that is used in the name generation.

        Returns
        -------
        packet: Dict[str, str]
            The data packet for a race which contains possible genders for names,
            source names, and the generator file that will be used in the url.
        '''
        # Establish file and return variables
        path: Path = Path('../data/name_generators.json').resolve()
        gen_dict: Dict[str, str]
        packet: Dict[str, str]
        
        # Open file and retrieve packet
        with open(path, 'r+') as f:
            gen_dict = loads(f.read())
            packet = {k: x for (k, x) in gen_dict.items() if k == race_name}

        return packet