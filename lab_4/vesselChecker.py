import pandas as pd
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

REQ_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
}

def extract_ship_props(soup):
    cells = soup.find_all('td')
    result = {"IMO": "Нет", "MMSI": "Нет", "AIS тип": "Нет"}

    for i in range(len(cells) - 1):
        key = cells[i].get_text().strip()
        val = cells[i + 1].get_text().strip()

        if "IMO" in key and "MMSI" in key:
            parts = val.split("/")
            result["IMO"] = parts[0].strip()
            result["MMSI"] = parts[1].strip()
        elif "IMO" in key:
            result["IMO"] = val
        elif "MMSI" in key:
            result["MMSI"] = val
        elif "AIS тип" in key:
            result["AIS тип"] = val

    return result

def fetch_ship_info(link):
    print(f"Парсинг {link[45:]}...")
    try:
        resp = requests.get(link, headers=REQ_HEADERS)
        if resp.status_code != 200:
            print(f"ОШИБКА с кодом {resp.status_code}")
            return None

        soup = BeautifulSoup(resp.content, 'html.parser')
        ship_links = soup.find_all('a', class_='ship-link')

        if len(ship_links) != 1:
            print("Не ровно один корабль")
            return None

        ship_url = f"https://vesselfinder.com{ship_links[0]['href']}"
        resp = requests.get(ship_url, headers=REQ_HEADERS)

        if resp.status_code != 200:
            print(f"ОШИБКА с кодом {resp.status_code}")
            return None

        soup = BeautifulSoup(resp.content, 'html.parser')
        ship_data = extract_ship_props(soup)
        ship_name = soup.find('h1', class_='title').get_text().strip()
        ship_data['Название'] = ship_name

        return ship_data
    except Exception as err:
        print(f"Возникло исключение: {err}")
        return None

links_df = pd.read_excel('Links.xlsx')
url_list = links_df['Ссылка'].tolist()

with ThreadPoolExecutor(max_workers=10) as pool:
    parsed_results = list(pool.map(fetch_ship_info, url_list))

clean_results = [item for item in parsed_results if item is not None]

result_df = pd.DataFrame(clean_results)
result_df = result_df[["Название", "IMO", "MMSI", "AIS тип"]]

result_df.to_excel('result.xlsx', index=False)
print("Файл result.xlsx успешно создан!")
