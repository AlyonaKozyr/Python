import requests
from bs4 import BeautifulSoup


def get_page(url):
    try:
        response = requests.get(url)
        if response.ok:
            return response.text
        else:
            print("Error " + str(response.status_code))
            return False
    except requests.exceptions.ConnectTimeout:  # если нет подключения
        print('Oops. Connection timeout occured!')
    except requests.exceptions.ReadTimeout:  # если истекло время ожидания
        print('Oops. Read timeout occured')
    except requests.exceptions.ConnectionError:  # если произошла ошибка соединения
        print('Seems like dns lookup failed..')


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []
    i = 0
    while i < 87:
        new = {'name': parser.table.findAll('table')[1].findAll('tr')[i].findAll('td')[2].a.text,
               'author': parser.table.findAll('table')[1].findAll('tr')[i+1].a.text,
               'likes': parser.table.findAll('table')[1].findAll('tr')[i+1].span.text,
               'comments': parser.table.findAll('table')[1].findAll('tr')[i+1].findAll('a')[-1].text,
               'link': parser.table.findAll('table')[1].findAll('tr')[i].findAll('td')[2].a['href']}
        news_list.append(new)
        i += 3
    return news_list


def extract_next_page(parser):
    """ Extract next page URL """
    more_link = parser.table.findAll('table')[1].findAll('a')[-1].get('href')
    return more_link


def get_news(url, n_pages=1):
    """ Collect news from a given web page and returns a dictionaries' list """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = get_page(url)
        soup = BeautifulSoup(response, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news


def sep_row(string):
    """ делит строчку на слова"""
    word = ''
    word_list = []
    for i in range(len(string)):
        if string[i] != ' ':
            word += string[i]
        else:
            word_list.append(word)
            word = ''
    word_list.append(word)
    return word_list
