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
                       name_amount: int = 1, gender: Union[List[str], str] = 'Default',
                       binary_path: str = 'Default'):
        '''

        '''
        self.race_name = race_name
        self.source = source
        self.name_amount = name_amount
        self.binary_path = binary_path
        self.gender = gender #type: ignore

    def generate_names(self, race_name: str = 'Default', 
                        gender: Union[List[str], str] = 'Default',
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

        #- [x] Add ability to call male or female names specifically.
        #- [x] Update name_generators.json to include gender information.
        #- [] Add feature to get only the specified amount of names total, instead of all
        #- [] Add packet ability to get names from multiple races and gender
        #  and return them as a json packet
        #- [] Add source filter to name_generator.json file

        # Adjust self variables if needed
        self.race_name = race_name if race_name else self.race_name
        self.source = source if source else self.source
        self.name_amount = name_amount if name_amount else self.name_amount
        self.gender = gender if gender else self.gender #type: ignore

        # Add return variable
        names: Union[List[str], str] = []
        names_text: str = ''
        result_tag: str = ''

        # Add options for chromedriver
        opts: Options = Options()
        opts.add_argument('--headless')
        opts.add_argument('--disable-gpu')

        # Get race information
        race_packet: Dict[str, str] = self.__get_packet()
        race_url: str = race_packet[self.race_name]['generator'] #type: ignore
        url: str = ''.join([self._base_url, race_url])

        # Get button & xpath information
        button_list: List[str] = self.__get_button_list(race_packet=race_packet)
        result_id: str = '//*[@id="result"]'

        # Get binary path from input
        binary_path: str = self.binary_path

        # Open browser and go to url
        browser: Any = webdriver.Chrome(executable_path=binary_path, options=opts) 
        browser.get(url=url)

        # Click button and append result_tag
        for button in button_list:
            input_button = browser.find_element_by_xpath(button)
            input_button.click()
            result_tag = WebDriverWait(
                driver=browser,
                timeout=10).until(
                    EC.presence_of_element_located(
                        (By.XPATH,
                        result_id))).find_element_by_xpath(result_id).text
            names_text += '\n' + result_tag
        names = names_text.splitlines()
        names.remove('')
        browser.quit()

        return names
    
    def __get_packet(self) -> Dict[str, str]:
        '''
        Retrieves the data packet for a given race name, filter by race.
        TODO:
        - [] Add source filter to function so it can be filtered on function.
        - [] Add ability to filter on a default or without input.

        Parameters
        ----------
        None

        Returns
        -------
        packet: Dict[str, str]
            The data packet for a race which contains possible gender for names,
            source names, and the generator file that will be used in the url.
        '''
        # Establish file and return variables
        path: Path = Path('../data/name_generators.json').resolve()
        gen_dict: Dict[str, str]
        packet: Dict[str, str]
        
        # Open file and retrieve packet
        with open(path, 'r+') as f:
            gen_dict = loads(f.read())
            packet = {k: x for (k, x) in gen_dict.items() if k == self.race_name}

        return packet
    
    def __get_button_list(self, race_packet: Dict[str, str]) -> List[str]:
        '''

        '''
        button_dict: Dict[str, str] = {
            "male": "/html/body/div/div[2]/div/div[4]/div[1]/input[1]",
            "female": "/html/body/div/div[2]/div/div[4]/div[1]/input[2]",
            "neutral": "/html/body/div/div[2]/div/div[4]/div[1]/input",
            "old male": "/html/body/div/div[2]/div/div[4]/div[1]/input[3]",
            "old female": "/html/body/div/div[2]/div/div[4]/div[1]/input[4]"
        }
        available_genders: List[str] = list(race_packet[self.race_name]['gender']) #type: ignore
        button_list: List[str] = [x for (k, x) in button_dict.items() if k in available_genders and (k in self.gender or k == self.gender)]
        return button_list