import calendar
from datetime import datetime
import pandas as pd
from dateutil.relativedelta import relativedelta

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
month_now = datetime.now().strftime('%Y-%m')
print(month_now)
month_last = datetime.now().date() - relativedelta(months=1)
print(month_last)
