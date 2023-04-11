import requests
import pprint
import csv


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
        # 不同参数指定不同区域,这里指定了云、贵、川、渝
        'jobArea': '060000,090000,250000,260000',
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
        # 可以直接指定爬取数据个数，经测试，最大值为20000
        'pageSize': '20000',
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
