import requests
from bs4 import BeautifulSoup
import csv
import time
import os
import argparse
import re
from urllib.parse import quote

def setup_session():
    # Создаем сессию для чтения страниц
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'CountryDataScraper/1.0'
    })
    return session

def get_page_content(session, country_name, cache_dir='cache'):
    os.makedirs(cache_dir, exist_ok=True)
    cache_file = os.path.join(cache_dir, f"{quote(country_name, safe='')}.html")
    
    # Пробуем загрузить из кэша
    if os.path.exists(cache_file):
        with open(cache_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.strip():
                return content
    
    # Прямой запрос к Википедии для получения полного HTML
    url = f"https://en.wikipedia.org/wiki/{country_name.replace(' ', '_')}"
    
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        
        # Сохраняем в кэш
        with open(cache_file, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        return response.text
        
    except requests.RequestException as e:
        print(f"Ошибка при загрузке страницы для {country_name}: {e}")
        return None

def extract_infobox_data(html_content, country_name):
    """Извлечение данных из инфобокса страны"""
    if not html_content:
        return None
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Ищем таблицу с основной информацией о стране
    infobox = soup.find('table', class_='infobox')
    
    if not infobox:
        print(f" Информация не найдена для {country_name}")
        return None
    
    print(f" Инофрмация найдена!")
    
    # Извлекаем данные из таблицы
    data = {
        'country': country_name,
        'capital': extract_capital_from_infobox(infobox),
        'area': extract_area_from_infobox(infobox),
        'population': extract_population_from_infobox(infobox)
    }
    
    return data

def extract_capital_from_infobox(infobox):
    # Ключевые слова для поиска столицы
    capital_keywords = ['Capital', 'Capital and largest city', 'Capital city']
    
    for keyword in capital_keywords:
        try:
            rows = infobox.find_all('tr')
            for row in rows:
                 if keyword.lower() in row.get_text().lower():
                    value_cell = row.find('td')
                    if value_cell:
                        capital = value_cell.find('a')
                        return capital.text      
                                  
        except Exception as e:
            print(f"Ошибка при поиске столицы: {e}")
    
    return "Not found"

def extract_area_from_infobox(infobox):
    area_keywords = ['Area']
    
    for keyword in area_keywords:
        try:
            rows = infobox.find_all('tr')
            for row in rows:
                 if keyword in row.get_text():
                    desired_row = row.find_next_sibling()
                    if desired_row:
                        value_cell = desired_row.find('td')
                        area_text = value_cell.get_text()
                        # Ищем число с km²
                        area_match = re.search(r'(\d[\d,\.]*)\s*(?:km²|km2|km)', area_text)
                        if area_match:
                            area = area_match.group(1)
                            try:
                                area = area.replace(',', '').replace(' ', '')
                                return int(float(area))
                            except ValueError:
                                continue
                                  
        except Exception as e:
            print(f"Ошибка при поиске площади: {e}")
        
    return "Not found"

def extract_population_from_infobox(infobox):
    population_keywords = ['Population']
    
    for keyword in population_keywords:
        try:
            rows = infobox.find_all('tr')
            for row in rows:
                 if keyword in row.get_text():
                    desired_row = row.find_next_sibling()
                    if desired_row:
                        value_cell = desired_row.find('td')
                        pop_text = value_cell.get_text()
                        numbers = re.findall(r'(\d[\d,\.]*)', pop_text)
                        if numbers:
                            population = numbers[0]
                            try:
                                population = population.replace(',', '').replace(' ', '')
                                return population
                            except ValueError:
                                continue
        except Exception as e:
            print(f"Ошибка при поиске населения: {e}")                       
    return "Not found"

def process_single_country(session, country_name, cache_dir):
    print(f" Обрабатывается: {country_name}")
    
    # Получаем полный HTML страницы
    html_content = get_page_content(session, country_name, cache_dir)
    
    if not html_content:
        print(f" Не удалось загрузить страницу для {country_name}")
        return None
    
    # Извлекаем данные из таблицы
    country_data = extract_infobox_data(html_content, country_name)
    
    if country_data:
        capital_display = country_data['capital'] if country_data['capital'] != "Not found" else "не найдена"
        area_display = f"{country_data['area']} km²" if country_data['area'] != "Not found" else "не найдена"
        pop_display = f"{country_data['population']}" if country_data['population'] != "Not found" else "не найдено"
        
        print(f" Данные получены: столица {capital_display}, площадь {area_display}, население {pop_display}")
        return country_data
    else:
        print(f" Не удалось извлечь данные для {country_name}")
        return None

def save_to_csv(data, output_file):
    if not data:
        print("Нет данных для сохранения")
        return
    
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['country', 'city', 'area', 'population'])
            writer.writeheader()
            
            for row in data:
                csv_row = {
                    'country': row['country'],
                    'city': row['capital'],
                    'area': row['area'],
                    'population': row['population']
                }
                writer.writerow(csv_row)
                
        print(f"Данные сохранены в {output_file}")
        
    except Exception as e:
        print(f"Ошибка при сохранении в CSV: {e}")

def read_countries_from_file(filename):
    try:        
        with open(filename, 'r', encoding='utf-8') as f:
            countries = [line.strip() for line in f if line.strip()]
        
        print(f" Прочитано {len(countries)} стран")
        return countries
        
    except Exception as e:
        print(f" Ошибка при чтении файла {filename}: {e}")
        return []

def main():
    
    # Читаем список стран
    countries = read_countries_from_file(filename='countries.txt')
    if not countries:
        print(" Создайте файл countries.txt со списком стран")
        return
    
    # Настраиваем сессию
    session = setup_session()
    
    results = []
    successful = 0
    
    # Обрабатываем каждую страну
    for i, country in enumerate(countries, 1):
        country_data = process_single_country(session, country, cache_dir='cache')
        
        if country_data:
            results.append(country_data)
            successful += 1
        
        # Пауза между запросами
        if i < len(countries):
            time.sleep(1)
    
    # Сохраняем результаты
    save_to_csv(results, output_file='countries_data.csv')
    
    print(f"\n Обработка завершена:")
    print(f"Успешно обработано: {successful}/{len(countries)}")

if __name__ == "__main__":
    main()