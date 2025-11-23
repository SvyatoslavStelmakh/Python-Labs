from bs4 import BeautifulSoup
import re
import requests
import wikipediaapi
import time

# Инициализация Wikipedia API
wiki = wikipediaapi.Wikipedia(
    user_agent='CountryParser/1.0 (gmail@example.com)',  
    language='en',                                         
    extract_format=wikipediaapi.ExtractFormat.WIKI        
)
   


def get_country_info(page, country_name):
    """Извлечение данных из инфобокса страны"""
    
    if not page:
        return None
    
    soup = BeautifulSoup(page, 'html.parser')
    
    # Ищем инфобокс страны
    infobox = soup.find('table', class_='infobox ib-country vcard')
    
    if not infobox:
        print(f"Не найден инфобокс для {country_name}")
        return None
    
    data = {
        'country': country_name,
        'capital': extract_capital_from_infobox(infobox),
        'area': extract_area(infobox),
        'population': extract_population(infobox)
    }
    
    return data

def extract_capital_from_infobox(infobox):
    """Извлечение столицы из инфобокса"""
    capital_keywords = ['Capital', 'Capitaland largest city', 'Capital city', 'Capital(s)']
    
    for keyword in capital_keywords:
        capital = find_infobox_value(infobox, keyword)
        if capital and capital != "Not found":
            # Очистка от ссылок и примечаний
            capital = re.sub(r'\[.*?\]', '', capital)
            capital = capital.split('[')[0].split('\n')[0].strip()
            # Убираем лишние символы и текст в скобках
            capital = re.sub(r'\(.*?\)', '', capital).strip()
            if capital and len(capital) > 1:
                return capital
    
    return "Not found"

def find_infobox_value(infobox, key):
    """Поиск значения по ключу в инфобоксе"""
    try:
        # Ищем строку с заголовком
        rows = infobox.find_all('tr')
        for row in rows:
            header = row.find('th')
            if header and key.lower() in header.get_text().lower():
                # Ищем значение в соседней ячейке
                value_cell = row.find('td')
                if value_cell:
                    return value_cell.get_text(strip=True)
        
        # Альтернативный поиск для некоторых структур
        for row in rows:
            if key.lower() in row.get_text().lower():
                value_cell = row.find('td')
                if value_cell:
                    return value_cell.get_text(strip=True)
                    
    except Exception as e:
        print(f"Ошибка при поиске значения '{key}': {e}")
    
    return "Not found"


def extract_capital(soup):
    """Извлекает столицу страны"""
    try:
        # Считываем таблицу с основной информацией о стране
        infobox = soup.find('table', class_='infobox ib-country vcard')     
        if infobox:
            rows = infobox.find_all('tr')  # записываем все строки таблицы в список
            # Теперь перебираем в цикле все строки таблицы 
            for row in rows:
                if 'Capital' in row.text:
                    capital_cell = row.find('td', class_='infobox-data')    # получаем ячейку таблицы с названием столицы и ее координатами
                    if capital_cell:
                        capital = capital_cell.find('a').text
                        return capital
    except:
        pass
    return "Not found"



def extract_area(soup):
    try:
        # Считываем таблицу с основной информацией о стране
        infobox = soup.find('table', class_='infobox ib-country vcard')     
        if infobox:
            rows = infobox.find_all('tr')  # записываем все строки таблицы в список
            # Теперь перебираем в цикле все строки таблицы 
            for row in rows:
                if 'Area' in row.text:
                    desired_row = row.find_next_sibling()   # информация о населении находится в следующей строке
                    area_cell = desired_row.find('td', class_='infobox-data')    # получаем ячейку таблицы с названием столицы и ее координатами
                    if area_cell:
                        area = area_cell.get_text(strip=True)
                        return area
    except:
        pass
    return "Not found"

def extract_population(soup):
    """Извлекает население страны"""
    try:
        infobox = soup.find('table', class_='infobox ib-country vcard')
        if infobox:
            rows =  infobox.find_all('tr')
            for row in rows:
                if 'Population' in row.text:
                    desired_row = row.find_next_sibling()   # информация о населении находится в следующей строке
                    population_cell = desired_row.find('td', class_='infobox-data')
                    if population_cell:
                        population = population_cell.get_text(strip=True)
                        return population
    except:
        pass
    return "Not found"

page = wiki.page('United_States')

print(get_country_info(page.text, 'United States'))