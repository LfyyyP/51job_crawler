import os
import requests
import csv
import pandas as pd
import hmac
from hashlib import sha256
import time
# from fake_useragent import UserAgent

# 真实网页地址，从Network模块中获取
url = 'https://cupidjob.51job.com/open/noauth/search-pc'
orign = '/open/noauth/search-pc?api_key=51job&timestamp=1681189650&keyword=plc&searchType=2&function=&industry' \
        '=&jobArea=070000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType' \
        '=&issueDate=&sortType=0&pageNum=1&requestId=&pageSize=50&source=1&accountId=&pageCode=sou%7Csou%7Csoulb'

# 浏览真实网页所需参数
data = {
    'api_key': '51job',
    'timestamp': '',
    'keyword': 'plc',
    'searchType': '2',
    'function': '',
    'industry': '',
    # 不同参数指定不同区域,这里指定了云、贵、川、渝
    'jobArea': '',
    'jobArea2': '',
    'landmark': '',
    'metro': '',
    'salary': '',
    'workYear': '',
    'degree': '',
    'companyType': '',
    'companySize': '',
    'jobType': '',
    # 发布日期筛选
    'issueDate': '',
    'sortType': '0',
    'pageNum': '1',
    'requestId': '',
    # 可以直接指定爬取数据个数，经测试，最大值为20000
    'pageSize': '20000',
    'source': '1',
    'accountId': '',
    'pageCode': 'sou|sou|soulb',
}
# 请求头
headers = {
    'sign': '21979efb8f05715fca87ba0a3eacf5fc9490d1f10c8714e6b8e899a17af30aee',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/111.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'From-Domain': '51job_web',
    'Host': 'cupidjob.51job.com',
    'Origin': 'https://we.51job.com',
    'Referer': 'https://we.51job.com/',
    'uuid': '37c1001f745692a4df81eb789dfe9003,'
}
cities_ = {
    '北京': '010000',
    '上海': '020000',
    '天津': '050000',
    '重庆': '060000',
    '广东': '030000',
    '江苏': '070000',
    '浙江': '080000',
    '四川': '090000',
    '海南': '100000',
    '福建': '110000',
    '山东': '120000',
    '江西': '130000',
    '广西': '140000',
    '安徽': '150000',
    '河北': '160000',
    '河南': '170000',
    '湖北': '180000',
    '湖南': '190000',
    '陕西': '200000',
    '山西': '210000',
    '黑龙江': '220000',
    '辽宁': '230000',
    '吉林': '240000',
    '云南': '250000',
    '贵州': '260000',
    '甘肃': '270000',
    '内蒙古': '280000',
    '宁夏': '290000',
    '西藏': '300000',
    '新疆': '310000',
    '青海': '320000',
}

column = ['company_name',
          'company_type',
          'company_size',
          'update_time',
          'job_name',
          'job_area',
          'job_tags',
          'salary',
          'company_link'
          ]


# 爬取数据
def craw_data(url, headers, data, column):
    response = requests.get(url=url, headers=headers, params=data)
    time.sleep(3)
    # 创建csv文件
    f = open('data.csv', mode='w', encoding='utf-8', newline='')
    csv_writer = csv.DictWriter(f, fieldnames=column)
    # 循环写入网页中的数据
    for index in response.json()['resultbody']['job']['items']:
        dit = {
            'company_name': index['fullCompanyName'],
            'company_type': index['companyTypeString'],
            'company_size': index['companySizeString'],
            'update_time': index['updateDateTime'],
            'job_name': index['jobName'],
            'job_area': index['jobAreaString'],
            'job_tags': index['jobTags'],
            'salary': index['provideSalaryString'],
            'company_link': index['companyHref'],
        }
        csv_writer.writerow(dit)
    return 0


def data_edit(city, keyWord):
    df = pd.read_csv('data.csv', names=column)
    # 去重
    df.drop_duplicates(keep='last', inplace=True)
    # 写成xlsx格式文件
    writer = pd.ExcelWriter('{} {} {}.xlsx'.format(keyWord, '_', city))
    df.to_excel(writer)
    writer.save()
    # 删除csv格式文件
    os.remove('data.csv')
    print('爬取完成！')
    return 0


def start_doing():
    print('欢迎来到51job数据爬虫！')
    keyWord = input('请输入想要搜索的关键词：')
    for i in list(cities_.keys()):
        print(i, end=' ')
    cityPrint = input('\n请输入想要爬取的城市名称(务必从上表中选取！)：')
    city = cities_[cityPrint]
    data['jobArea'] = city
    data['keyword'] = keyWord
    # 构造sign参数
    now = str(int(time.time()))
    data_1 = '/open/noauth/search-pc?api_key=51job&'
    data_2 = 'timestamp=' + now
    data_3 = 'keyword=' + data['keyword']
    data_4 = 'searchType=2&function=&industry=&'
    data_5 = 'jobArea=' + data['jobArea']
    data_6 = 'jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate' \
             '=&sortType=0&pageNum=1&requestId=&pageSize=20&source=1&accountId=&pageCode=sou%7Csou%7Csoulb'
    speStr = '&'
    backAddr = data_1 + data_2 + speStr + data_3 + speStr + data_4 + data_5 + speStr + data_6
    sign = get_sign(backAddr)
    # print(sign)
    # print(backAddr)
    headers['sign'] = sign
    # 构造UserAgent
    # fake_headers = {"user-agent": UserAgent().random}
    # headers['User-Agent'] = fake_headers['user-agent']
    # 构造fakeIP
    print('请等待爬取过程！')
    return cityPrint, keyWord


#  获取签名
def get_sign(data):
    key = 'abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b'
    key = key.encode('utf-8')
    message = data.encode('utf-8')
    sign = hmac.new(key, message, digestmod=sha256).hexdigest()
    return sign


if __name__ == '__main__':
    while True:
        fileName, keyWord = start_doing()
        craw_data(url, headers, data, column)
        data_edit(fileName, keyWord)
        exCon = input('是否继续爬取？继续：输入1 退出：输入0：')
        if exCon == '0':
            break
