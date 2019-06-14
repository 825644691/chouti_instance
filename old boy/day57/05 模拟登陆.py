import requests


###首先登陆任何页面，获取cookies
i1 = requests.get(url="http://dig.chouti.com")

###用户登陆，携带上一次的cookies，后台对cookies中的gpsd进行授权
i2 = requests.post(
    url="http://dig.chouti.com/login/",
    data = {
        "phone":"86手机号",
        "password":"密码",
        "oneMonth": ""
    },
    cookies=i1.cookies.get_dict()
)


###点赞,(只要携带已经被授权的gpsd即可)
gpsd = i1.cookies.get_dict()['gpsd']
i3 = requests.post(
    url="http://dig.chouti.com/link/vote?linksId=854561",
    cookies={"gpsd":gpsd}
)
print(i3.text)