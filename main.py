from selenium import webdriver
import time
from bs4 import BeautifulSoup

def get_html(url):

    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--headless') #Работа браузера в фоновом режиме
    options_chrome.add_argument('user-data-dir=C:\\Users\\OlegGrigorev\\AppData\\Local\\Google\\Chrome\\User Data') #Здесь надо прописать путь к своей папке User Data

    driver = webdriver.Chrome(options=options_chrome)
    url = url.replace('40', '1000') #Здесь мы меняем в ссылке значение [per_page], что бы после разового скроллинга загрузилась вся инфа
    driver.get(url)

    scroll_by = f'window.scrollBy(0, document.body.scrollHeight);'
    driver.execute_script(scroll_by)
    time.sleep(1)

    return driver.page_source #возвращаем код страницы


# Пример работы
start_time = time.time() #Время начала работы функции
html = get_html('https://vk.com/friends?act=find&c[bday]=14&c[byear]=2004&c[city]=1,1&c[name]=1&c[per_page]=40&c[photo]=1&c[q]=%D0%BC%D0%B0%D1%80%D0%B8%D1%8F&c[section]=people') #Получаем html
end_time = time.time() #Время окончания работы функции

soup = BeautifulSoup(html, 'html.parser')# Скармиваем в BeautifulSoup (lxml здесь лучше не использовать)

divs = soup.find_all('div', 'people_row search_row clear_fix') #Ищем все блоки с инфой о людях

list_id = [x.find('a')['href'] for x in divs] # извлекаем атрибуты href из каждого div, формируя из этого список

print(list_id) # сам список ID
print('Количесво ID в списке:', len(list_id))
print(f'Функци работала {end_time - start_time } сек.')