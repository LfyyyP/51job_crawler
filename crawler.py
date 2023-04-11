import requests
import pprint
import csv
import hmac
from hashlib import sha256


#  获取签名
def get_sign(data):
    key = 'abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b'
    key = key.encode('utf-8')
    message = data.encode('utf-8')
    sign = hmac.new(key, message, digestmod=sha256).hexdigest()
    return sign


# 爬取数据
def craw_data(url, headers, data):
    response = requests.get(url=url, headers=headers, params=data)
    # 创建csv文件
    f = open('data.csv', mode='a', encoding='utf-8', newline='')
    csv_writer = csv.DictWriter(f, fieldnames=[
        'company_name',
        'company_type',
        'company_size',
        'update_time',
        'job_name',
        'job_area',
        'job_tags',
        'salary',
        'company_link',
    ])
    # 循环写入网页中的数据
    for index in response.json()['resultbody']['job']['items']:
        dit = {
            'company_name': index['companyName'],
            'company_type': index['companyTypeString'],
            'company_size': index['companySizeString'],
            'update_time': index['updateDateTime'],
            'job_name': index['jobName'],
            'job_area': index['jobAreaString'],
            'job_tags': index['jobTags'],
            'salary': index['provideSalaryString'],
            'company_link': index['companyHref'],
        }
        print(dit)
        csv_writer.writerow(dit)


if __name__ == '__main__':
    # 真实网页地址，从Network模块中获取
    url = 'https://cupidjob.51job.com/open/noauth/search-pc'
    # 浏览真实网页所需参数
    data = {
        'api_key': '51job',
        'timestamp': '1681188460',
        'keyword': 'plc',
        'searchType': '2',
        'function': '',
        'industry': '',
        'jobArea': '070000',
        'jobArea2': '',
        'landmark': '',
        'metro': '',
        'salary': '',
        'workYear': '',
        'degree': '',
        'companyType': '',
        'companySize': '',
        'jobType': '',
        'issueDate': '',
        'sortType': '0',
        'pageNum': '1',
        'requestId': '',
        'pageSize': '120',
        'source': '1',
        'accountId': '',
        'pageCode': 'sou|sou|soulb',
    }
    # 请求头
    headers = {
        'sign': '593b36966e1fea654dd4576286192213fdfab0aac4c0bdbcabdd314cd672416c',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }
    craw_data(url, headers, data)
    # data_1 = '/open/noauth/search-pc?api_key=51job&timestamp=1681189650&keyword=plc&searchType=2&function=&industry=&jobArea=070000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum=1&requestId=&pageSize=50&source=1&accountId=&pageCode=sou%7Csou%7Csoulb'
    # sign = get_sign(data=data_1)
    # print(sign)
