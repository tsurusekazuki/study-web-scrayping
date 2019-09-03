import requests
from bs4 import BeautifulSoup


def main():
    # スクレイピング先のURL
    url = 'https://kitnet.jp/laboratories/'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'lxml')
    subjectBody = soup.select('.subjectBody')
    print(subjectBody)


if __name__ == '__main__':
    main()