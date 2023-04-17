import time
import pandas as pd

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
df = pd.read_csv('data.csv', names=column)
time_list = df['update_time']
timestamp = []
for i in time_list:
    timeArray = time.strptime(i, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    timestamp.append(timeStamp)

# # 获得当前时间时间戳
# now = int(time.time())
# # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
# timeArray = time.localtime(now)
# otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
# print(otherStyleTime)
