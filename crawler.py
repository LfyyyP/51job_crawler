import requests
import pprint
import csv


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
url = 'https://cupidjob.51job.com/open/noauth/search-pc'
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
    'pageNum': '2',
    'requestId': '',
    'pageSize': '50',
    'source': '1',
    'accountId': '',
    'pageCode': 'sou|sou|soulb',
}
headers = {
    'sign': '593b36966e1fea654dd4576286192213fdfab0aac4c0bdbcabdd314cd672416c',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}
response = requests.get(url=url, headers=headers, params=data)
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
