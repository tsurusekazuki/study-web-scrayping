import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://kitnet.jp/laboratories/'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'lxml')

    dept_name = soup.select('.deptName')

    for d_n in dept_name:
        print(d_n.text)


if __name__ == "__main__":
    main()