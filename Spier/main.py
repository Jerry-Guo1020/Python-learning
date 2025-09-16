import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0.0.0 Safari/537.36"
}



def get_praise():
    praise_list = []
    for i in range(0, 2000, 20):
        url = 'https://movie.douban.com/subject/3878007/comments?start=%s&limit=20&sort=new_score&status=P&percent_type=h' % str(i)
        req = requests.get(url, headers=headers).text
        content = BeautifulSoup(req, "html.parser")

        # 防止没有 title 报错
        title_tag = content.title
        if not title_tag:
            print(f"第 {i} 页获取失败，可能被反爬。URL: {url}")
            break

        check_point = content.title.string
        if check_point != r"没有访问权限":
            comment = content.find_all("span", attrs={"class": "short"})
            for k in comment:
                praise_list.append(k.string)
        else:
                break
    return praise_list

def get_ordinary():
    high_list = []
    for i in range(0, 2000, 20):
        url = 'https://movie.douban.com/subject/3878007/comments?start=%s&limit=20&sort=new_score&status=P&percent_type=m'% str(i)
        req = requests.get(url, headers=headers).text
        content = BeautifulSoup(req, "html.parser")

        title_tag = content.title
        if not title_tag:
            print(f"第 {i} 页获取失败，可能被反爬。URL: {url}")
            break

        check_point = content.title.string
        if check_point != r'没有访问权限':
            comment = content.find_all("span", attrs={"class": "short"})
            for k in comment:
                high_list.append(k.string)
        else:
            break
    return high_list



def get_lowest():
    lowest_list = []
    for i in range(0, 2000, 20):
        url = 'https://movie.douban.com/subject/3878007/comments?start=%s&limit=20&sort=new_score&status=P&percent_type=l'% str(i)
        req = requests.get(url, headers=headers).text
        content = BeautifulSoup(req, "html.parser")

        title_tag = content.title
        if not title_tag:
            print(f"第 {i} 页获取失败，可能被反爬。URL: {url}")
            break


        check_point = content.title.string
        if check_point != r'没有访问权限':
            comment = content.find_all("span", attrs={"class": "short"})
            for k in comment:
                lowest_list.append(k.string)
        else:
            break
    return lowest_list


if __name__ == "__main__":
    print("正在获取信息……")
    praise_data = get_praise()

    print("正在获取好评的消息……")
    ordinary_data = get_ordinary()

    print("正在获取差评的消息……")
    lowest_data = get_lowest()

    print("正在保存信息……")
    praise_pd = pd.DataFrame(columns=['praise_comment'], data=praise_data)
    praise_pd.to_csv('praise.csv', encoding='utf-8')
    print("正在保存好评信息……")
    ordinary_pd = pd.DataFrame(columns=['ordinary_comment'], data=ordinary_data)
    ordinary_pd.to_csv('ordinary.csv', encoding='utf-8')
    print("正在保存差评信息……")
    lowest_pd = pd.DataFrame(columns=['lowest_comment'], data=lowest_data)
    lowest_pd.to_csv('lowest.csv', encoding='utf-8')
    print("结束!!!")
