import pandas as pd


# 选择云贵川渝的数据，并进行日期和关键词的筛选
def select():
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
    # print('去重前共有重复值个数：', df.duplicated().sum(), '去重前共有重复值个数：', len(df))
    df.drop_duplicates(keep='last', inplace=True)
    # print('去重前共有重复值个数：', df.duplicated().sum(), '去重前共有重复值个数：', len(df))

    # 去掉含有一些关键词的数据
    """关键词列表"""
    wish_drop = ['嵌入', 'Linux', 'C#', 'Android', 'Android', '单片机', 'C语言']
    for i in wish_drop:
        df.drop(df[df['job_name'].str.contains(pat=i, regex=False)].index, inplace=True)
    """筛选出近期数据"""
    wish_date = '2023-03-01'
    df.drop(df[df['update_time'] <= wish_date].index, inplace=True)

    # 挑选出重庆的数据
    select_cq = df.loc[df['job_area'].str.contains('重庆'), :]
    # 挑选出云南的数据
    select_yn = df.loc[df['job_area'].str.contains(
        '云南|昆明|曲靖|玉溪|保山|昭通|丽江|普洱|临沧|大理|红河州|楚雄|德宏|文山|迪庆'), :]
    # 挑选出四川的数据
    select_sc = df.loc[df['job_area'].str.contains(
        '四川|成都|自贡|攀枝花|泸州|德阳|绵阳|广元|遂宁|内江|乐山|南充|眉山|宜宾|广安|达州|雅安|巴中|资阳|西昌'), :]
    # 挑选出四川的数据
    select_gz = df.loc[df['job_area'].str.contains('贵州|贵阳|六盘水|遵义|安顺|毕节|铜仁|黔'), :]
    combine_list = [select_cq, select_yn, select_sc, select_gz]
    return combine_list
    # print(ygcy.head(10))
    # df = df.append(ygcy)
    # df = df.drop_duplicates(subset=column, keep=False)
    # print(len(df))
    # print(df.head(10))
    # df = pd.DataFrame(df)
    # df.to_csv('test.csv')
    # a = pd.merge(df, ygcy, on=column)


# 输出csv文件
def write_csv(final_list):
    final_list = pd.DataFrame(final_list)
    final_list.to_csv('云贵川渝.csv')
    return 0


# 输出excel文件
def write_excel(province_list):
    writer = pd.ExcelWriter('云贵川渝.xlsx')
    # 建立四个sheet
    province_list[0].to_excel(writer, '重庆市')
    province_list[1].to_excel(writer, '云南省')
    province_list[2].to_excel(writer, '四川省')
    province_list[3].to_excel(writer, '贵州省')
    writer.save()
    return 0


if __name__ == '__main__':
    ty_form = select()
    write_excel(ty_form)
