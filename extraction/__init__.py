import requests
from bs4 import BeautifulSoup

def ekstrasi_data():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/112.0.0.0 Safari/537.36'}

        content = requests.get('https://artinamericaguide.com/listings', headers=headers)
        #print(content)
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        # print(soup.prettify())
        result = soup.find('div', {'class': "grid__item"})
        result = result.findChildren('h2')

        i = 1
        for res in result:
            print(i, res)
        #     # name = res.find('h2', 'card__title')
        #     # print("berapa kali", res)
        #     # print("Name : ", name)
        #     i = i + 1

        hasil = dict()
        hasil['name'] = soup.find('h2', 'card__title')
        hasil['description'] = 'description'
    else:
        print("else")
        return None
    return hasil

def tampilkan_data(result):
    if result is None:
        print("tidak bisa menemukan data gempa terkini")
        return
    #print(f"Name : {result['name']}")
    print(f"Description : {result['description']}")





