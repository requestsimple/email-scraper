from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re

user_url = str(input('[*] Enter Target URL To Scan: '))
count = int(input('[*] Enter how many emails you want to get: '))  # Исправил здесь для корректного ввода
urls = deque([user_url])
scraped_urls = set()
emails = set()

while len(urls):
    if len(emails) >= count:  # Проверяем, что количество найденных email не превышает count
        break
    url = urls.popleft()
    base_url = '{0.scheme}://{0.netloc}'.format(urllib.parse.urlparse(url))
    path = url[url.find(base_url) + len(base_url):]
    if path == '':
        path = '/'
    print(f'[*] Processing {len(emails)} - {url}')
    try:
        # Обрабатываем ссылки с mailto: для извлечения адресов электронной почты
        if url.startswith('mailto:'):
            email = url[7:]  # Убираем 'mailto:' и сохраняем адрес
            emails.add(email)
            continue
        response = requests.get(url)
    except requests.exceptions.MissingSchema:
        continue
    except requests.exceptions.ConnectionError:
        continue

    # Извлекаем электронные почты с веб-страницы
    new_emails = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', response.text, re.I))
    emails.update(new_emails)

    soup = BeautifulSoup(response.text, features='html.parser')
    for anchor in soup.find_all('a'):
        link = anchor.get('href', '')
        if link and not link.startswith('http'):
            if link.startswith('/'):
                link = base_url + link
        if link and link not in scraped_urls:
            scraped_urls.add(link)
            urls.append(link)

print('\n[*] Closing!\n')
for mail in emails:
    print(mail)
