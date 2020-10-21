'''
Main function meant to launch the thing I'm making
==================================================
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def main():
    '''
    Main function meant to pull data from the web

    '''
    binary_path: str = "C:\Program Files (x86)\chromedriver.exe"
    url: str = 'https://fantasynamegenerators.com/dnd-aasimar-names.php'
    opts: Options = Options()
    opts.add_argument('--headless')
    opts.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path=binary_path, options=opts)
    driver.get(url)
    driver.quit()

if __name__ == "__main__":
    main()