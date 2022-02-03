import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt



HOST = "https://animekisa.tv"

URL = "https://animekisa.tv/latest/1"

HOST_2 = "https://knigki.net"

URL_2 = "https://knigki.net/audioknigi/"

HOST_3 = "https://onlinemultfilmy.ru/"

URL_3 = "https://onlinemultfilmy.ru/anime/"


HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
}



@csrf_exempt

def get_html(url, params=""):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

@csrf_exempt

def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="episode-box test")
    anime = []

    for item in items:
        anime.append(
            {
                "title": item.find("div", class_="title-box-2").get_text(strip=True),
                "image": HOST + item.find("div", class_="image-box").find("img").get("src")
            }
        )
    print(anime)
    return anime

@csrf_exempt

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        anime = []
        for page in range(0, 1):
            html = get_html(URL, params={"page": page})
            anime.extend(get_content(html.text))
            return anime
    else:
        raise ValueError("Error in ANIME PARSER")


########################################################################################################################


@csrf_exempt

def get_html(url_2, params=""):
    req = requests.get(url_2, headers=HEADERS, params=params)
    return req

@csrf_exempt

def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="album-item")
    books = []

    for item in items:
        books.append(
            {
                "title": item.find("div", class_="album-title").get_text(strip=True),
                "image": HOST_2 + item.find("div", class_="album-img img-resp-sq img-fit").find("img").get("src")
            }
        )
    print(books)
    return books

@csrf_exempt

def parser():
    html = get_html(URL_2)
    if html.status_code == 200:
        books = []
        for page in range(0, 1):
            html = get_html(URL_2, params={"page": page})
            books.extend(get_content(html.text))
            return books
    else:
        raise ValueError("Error in BOOKS PARSER")

################################################################
# @csrf_exempt
#
# def get_html(url_3, params=""):
#     req = requests.get(url_3, headers=HEADERS, params=params)
#     return req
#
# @csrf_exempt
#
# def get_content(html):
#     soup = BeautifulSoup(html, "html.parser")
#     items = soup.find_all('div', class_='b-content__inline_items')
#     films = []
#
#     for item in items:
#         films.append(
#             {
#                 'title': item.find('div', class_='b-content__inline_item-link').get_text(strip=True),
#                 'image': HOST_3 + item.find('div', class_='b-content__inline_item-cover').find('img').get('src')
#             })
#     print(films)
#     return films
#
# @csrf_exempt
#
# def parser():
#     html = get_html(URL_3)
#     if html.status_code == 200:
#         films = []
#         for page in range(0, 1):
#             html = get_html(URL_3, params={"page": page})
#             films.extend(get_content(html.text))
#             return films
#     else:
#         raise ValueError("Error in FILMS PARSER")