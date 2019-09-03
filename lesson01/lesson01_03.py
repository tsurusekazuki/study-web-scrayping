import requests
from bs4 import BeautifulSoup


def is_lab_name_last(lab_name):
    lab_name_last = ['福江高志研究室', '赤坂剛史研究室', '村尾俊幸研究室', '柳橋秀幸研究室', '佐野渉二研究室', '花岡大伸研究室', '坂知樹研究室', '北川達也研究室', '石黒千晶研究室', '佐藤弘美研究室', '岡田豪研究室', '松本恵子研究室']
    return lab_name in lab_name_last

def main():
    url = 'https://kitnet.jp/laboratories/'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'lxml')
    lab_dict = {}
    school_subject_title_list = soup.select('.subjectTitle > .title')
    lab_name_list = soup.select('.laboList > ul > li > a')

    cnt = 0
    end_step = len(lab_name_list) - 1

    for s_s_t in school_subject_title_list:

        school_subject_title = s_s_t.text
        lab_dict[school_subject_title] = []

        for _ in range(30):

            lab_name = lab_name_list[cnt].text
            lab_dict[school_subject_title].append(lab_name)

            if cnt == end_step:
                break

            cnt += 1

            if is_lab_name_last(lab_name):
                break

    for key, value in lab_dict.items():
        print(key)
        print(value)
        print('---------------------------------------')


if __name__ == '__main__':
    main()