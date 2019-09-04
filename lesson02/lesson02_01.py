from bs4 import BeautifulSoup
import requests
import cchardet
import pandas as pd


class Shouchu:
    def __init__(self, start, end, url):
        self.start = start
        self.end = end
        self.url = url
        self.cnt = 0
        self.shouchu_dict = {
            'id': [],
            'name': [],
            'type': [],
            'locality': [],
            'frequency': [],
            'taste': []
        }

    def scr(self):
        for i in range(self.start, self.end + 1):
            next_url = self.url + '?act=sake_detail&id={}'.format(str(i))
            html = requests.get(next_url)
            html.encoding = cchardet.detect(html.content)["encoding"]
            soup = BeautifulSoup(html.content, "html.parser")
            texts = soup.select('.sakeInfoData > dl > dd')
            self.cnt += 1
            for j, text in zip(range(len(texts)), texts):
                sake_text = text.getText().replace('\u3000', '').strip().replace('\n', '').replace('\r', '').replace(
                    '\t', '')
                if j == 0:
                    self.shouchu_dict['id'].append(self.cnt)
                    self.shouchu_dict['name'].append(sake_text)
                if j == 1:
                    self.shouchu_dict['type'].append(sake_text)
                if j == 2:
                    self.shouchu_dict['locality'].append(sake_text)
                if j == 6:
                    self.shouchu_dict['frequency'].append(sake_text)
                if j == 7:
                    review_cnt = 1
                    for s_t in sake_text:
                        if s_t == '・':
                            review_cnt += 1
                        elif s_t == '★':
                            break
                    self.shouchu_dict['taste'].append(review_cnt)

        return self.shouchu_dict


class Wine:
    def __init__(self, start, end, url):
        self.start = start
        self.end = end
        self.url = url
        self.cnt = 0
        self.wine_dict = {
            'id': [],
            'name': [],
            'type': [],
            'locality': [],
            'taste': []
        }

    def scr(self):
        for i in range(self.start, self.end + 1):
            next_url = self.url + '?act=sake_detail&id={}'.format(str(i))
            html = requests.get(next_url)
            html.encoding = cchardet.detect(html.content)["encoding"]
            soup = BeautifulSoup(html.content, "html.parser")
            texts = soup.select('.sakeInfoData > dl > dd')
            self.cnt += 1
            for j, text in zip(range(len(texts)), texts):
                sake_text = text.getText().replace('\u3000', '').strip().replace('\n', '').replace('\r', '').replace(
                    '\t', '')
                if j == 0:
                    self.wine_dict['id'].append(self.cnt)
                    self.wine_dict['name'].append(sake_text)
                if j == 1:
                    self.wine_dict['type'].append(sake_text)
                if j == 2:
                    self.wine_dict['locality'].append(sake_text)
                if j == 3:
                    review_cnt = 1
                    for s_t in sake_text:
                        if s_t == '・':
                            review_cnt += 1
                        elif s_t == '★':
                            break
                    self.wine_dict['taste'].append(review_cnt)

        return self.wine_dict


class Sake:
    def __init__(self, start, end, url):
        self.start = start
        self.end = end
        self.url = url
        self.cnt = 0
        self.sake_dict = {
            'id': [],
            'name': [],
            'type': [],
            'locality': [],
            'frequency': [],
            'taste': []
        }

    def scr(self):
        for i in range(self.start, self.end + 1):
            next_url = self.url + '?act=sake_detail&id={}'.format(str(i))
            html = requests.get(next_url)
            html.encoding = cchardet.detect(html.content)["encoding"]
            soup = BeautifulSoup(html.content, "html.parser")
            texts = soup.select('.sakeInfoData > dl > dd')
            self.cnt += 1
            for j, text in zip(range(len(texts)), texts):
                sake_text = text.getText().replace('\u3000', '').strip().replace('\n', '').replace('\r', '').replace(
                    '\t', '')
                if j == 0:
                    self.sake_dict['id'].append(self.cnt)
                    self.sake_dict['name'].append(sake_text)
                if j == 1:
                    self.sake_dict['type'].append(sake_text)
                if j == 4:
                    self.sake_dict['locality'].append(sake_text)
                if j == 7:
                    self.sake_dict['frequency'].append(sake_text)
                if j == 8:
                    review_cnt = 1
                    for s_t in sake_text:
                        if s_t == '・':
                            review_cnt += 1
                        elif s_t == '★':
                            break
                    self.sake_dict['taste'].append(review_cnt)

        return self.sake_dict


class Beer:
    def __init__(self, start, end, url):
        self.start = start
        self.end = end
        self.url = url
        self.cnt = 0
        self.beer_dict = {
            'id': [],
            'name': [],
            'frequency': []
        }

    def scr(self):
        for i in range(self.start, self.end + 1):
            next_url = self.url + '?act=sake_detail&id={}'.format(str(i))
            html = requests.get(next_url)
            html.encoding = cchardet.detect(html.content)["encoding"]
            soup = BeautifulSoup(html.content, "html.parser")
            texts = soup.select('.sakeInfoData > dl > dd')
            self.cnt += 1
            for j, text in zip(range(len(texts)), texts):
                sake_text = text.getText().replace('\u3000', '').strip().replace('\n', '').replace('\r', '').replace(
                    '\t', '')
                if j == 0:
                    self.beer_dict['id'].append(self.cnt)
                    self.beer_dict['name'].append(sake_text)
                if j == 1:
                    self.beer_dict['frequency'].append(sake_text)

        return self.beer_dict


class Ume:
    def __init__(self, start, end, url):
        self.start = start
        self.end = end
        self.url = url
        self.cnt = 0
        self.ume_dict = {
            'id': [],
            'name': [],
            'type': [],
            'locality': [],
            'frequency': [],
            'taste': []
        }

    def scr(self):
        for i in range(self.start, self.end + 1):
            next_url = self.url + '?act=sake_detail&id={}'.format(str(i))
            html = requests.get(next_url)
            html.encoding = cchardet.detect(html.content)["encoding"]
            soup = BeautifulSoup(html.content, "html.parser")
            texts = soup.select('.sakeInfoData > dl > dd')
            self.cnt += 1
            for j, text in zip(range(len(texts)), texts):
                sake_text = text.getText().replace('\u3000', '').strip().replace('\n', '').replace('\r', '').replace(
                    '\t', '')
                if j == 0:
                    self.ume_dict['id'].append(self.cnt)
                    self.ume_dict['name'].append(sake_text)
                if j == 1:
                    self.ume_dict['type'].append(sake_text)
                if j == 2:
                    self.ume_dict['locality'].append(sake_text)
                if j == 4:
                    self.ume_dict['frequency'].append(sake_text)
                if j == 5:
                    review_cnt = 1
                    for s_t in sake_text:
                        if s_t == '・':
                            review_cnt += 1
                        elif s_t == '★':
                            break
                    self.ume_dict['taste'].append(review_cnt)

        return self.ume_dict


def dict_to_df(d):
    d2 = {}
    for k, v in d.items():  # 一度pd.Seriesに変換
        d2[k] = pd.Series(v)

    df = pd.DataFrame(d2)
    return df


def main():
    url = 'http://www.nomitomo.ne.jp/'
    shouchu = Shouchu(14, 20, url)
    shouchu_df = dict_to_df(shouchu.scr())
    print(shouchu_df)

    wine = Wine(435, 440, url)
    wine_df = dict_to_df(wine.scr())
    print(wine_df)

    sake = Sake(191, 200, url)
    sake_df = dict_to_df(sake.scr())
    print(sake_df)

    beer = Beer(569, 580, url)
    beer_df = dict_to_df(beer.scr())
    print(beer_df)

    ume = Ume(321, 330, url)
    ume_df = dict_to_df(ume.scr())
    print(ume_df)


if __name__ == "__main__":
    main()