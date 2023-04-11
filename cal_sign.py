import hmac
from hashlib import sha256


#  获取签名
def get_sign(data):
    key = 'abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b'
    key = key.encode('utf-8')
    message = data.encode('utf-8')
    sign = hmac.new(key, message, digestmod=sha256).hexdigest()
    return sign


if __name__ == '__main__':
    data_1 = '/open/noauth/search-pc?api_key=51job&timestamp=1681189650&keyword=plc&searchType=2&function=&industry=&jobArea=070000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum=1&requestId=&pageSize=50&source=1&accountId=&pageCode=sou%7Csou%7Csoulb'
    sign = get_sign(data=data_1)
    print(sign)