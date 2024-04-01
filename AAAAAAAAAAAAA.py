import requests
from bs4 import BeautifulSoup
def parse():
    page = requests.get('https://omgtu.ru/ecab/persons/index.php?b=11',verify= False)
    print(page.status_code)
    page_parsed = BeautifulSoup(page.text, 'html.parser')
    employees = page_parsed.findAll('div', style="padding: 5px; font-size: 120%;")
    with open('result.txt', 'w') as f:
        for employee in employees:
            name = employee.find('a').text.strip()
            f.write(name + '\n')
if __name__ == '__main__':
    parse()