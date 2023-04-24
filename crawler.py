import os
import requests
import csv
import pandas as pd

# 真实网页地址，从Network模块中获取
url = 'https://cupidjob.51job.com/open/noauth/search-pc'
# 浏览真实网页所需参数
data = {
    'api_key': '51job',
    'timestamp': '1681701772',
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
    'pageSize': '10000',
    'source': '1',
    'accountId': '',
    'pageCode': 'sou|sou|soulb',
}
# 请求头
headers = {
    'sign': '21979efb8f05715fca87ba0a3eacf5fc9490d1f10c8714e6b8e899a17af30aee',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/111.0.0.0 Safari/537.36',
}
cities_ = {
    '北京': '010000,',
    '上海': '020000,',
    '天津': '050000,',
    '重庆': '060000,',
    '广东': '030000,',
    '江苏': '070000,',
    '浙江': '080000,',
    '四川': '090000,',
    '海南': '100000,',
    '福建': '110000,',
    '山东': '120000,',
    '江西': '130000,',
    '广西': '140000,',
    '安徽': '150000,',
    '河北': '160000,',
    '河南': '170000,',
    '湖北': '180000,',
    '湖南': '190000,',
    '陕西': '200000,',
    '山西': '210000,',
    '黑龙江': '220000,',
    '辽宁': '230000,',
    '吉林': '240000,',
    '云南': '250000,',
    '贵州': '260000,',
    '甘肃': '270000,',
    '内蒙古': '280000,',
    '宁夏': '290000,',
    '西藏': '300000,',
    '新疆': '310000,',
    '青海': '320000,',
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
    # 创建csv文件
    f = open('data.csv', mode='a', encoding='utf-8', newline='')
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


def data_edit():
    df = pd.read_csv('data.csv', names=column)
    # 去重
    df.drop_duplicates(keep='last', inplace=True)
    # 写成xlsx格式文件
    writer = pd.ExcelWriter('客户数据.xlsx')
    df.to_excel(writer)
    writer.save()
    # 删除csv格式文件
    os.remove('data.csv')
    print('爬取完成！')
    return 0


def start_doing():
    print('欢迎来到51job数据爬虫！\n', '如需连续爬取，请务必将上一次爬取结果重命名！')
    for i in list(cities_.keys()):
        print(i, end=' ')
    city = input('\n请输入想要搜索的关键词：')
    area = input('请输入想要爬取的城市名称(务必从上表中选取！)：')
    area = cities_[area]
    data['jobArea'] = area
    data['keyword'] = city
    print('请等待爬取过程！')
    return 0


if __name__ == '__main__':
    start_doing()
    craw_data(url, headers, data, column)
    data_edit()
