import requests
import re


url='http://www.12365auto.com/js/brandsHaveSeries.js?version=20210207'
headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'td_cookie=1068896930; uuid_visit_refdm=www.12365auto.com; UM_distinctid=176a85bf8f857-0fc62d1258f149-c791039-1fa400-176a85bf8f93f2; aliyungf_tc=210b9ba644483e087031963aa1311c6fd5c3cdef2e9f2812058e49e425e3ae4e; td_cookie=2534554653; uuid_visit_refdm=www.12365auto.com; CNZZDATA2115974=cnzz_eid%3D1106447967-1609138644-http%253A%252F%252Fwww.12365auto.com%252F%26ntime%3D1612656280; uuid=1259423673286528; Hm_lvt_d08ac25fd4c45e85e8d9f1c32e97a0eb=1611195437,1612661351; ASP.NET_SessionId=stdemr554k3pg4zjkvpi32ul; uuid_visit_dltime=1612661592619; Hm_lpvt_d08ac25fd4c45e85e8d9f1c32e97a0eb=1612661593',
'Host': 'www.12365auto.com',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

response_car_info=requests.get(headers=headers,url=url)
print(response_car_info.status_code)
brands_pattern=re.compile(r'{"id":"(.*?)","name":"(.*?)","initials"')
# series_pattern=re.compile(r'<select id="series"> (.*?) </select>')
# models_pattern=re.compile(r'<select id="models"> (.*?) </select>')
brands=brands_pattern.findall(response_car_info.text)
brand_list=[]
for i in brands:
    brand_temp={'id':i[0],'brand':i[1]}
    brand_list.append(brand_temp)
print(brand_list)
url_pattern='http://www.12365auto.com/zlts/{}-0-0-0-0-0_0-0-0-0-0-0-0-{}.shtml'
url_list=[]
page=1
for i in brand_list:
    temp={'brand':i['brand'],'url':url_pattern.format(i['id'],page)}
    url_list.append(temp)
print(url_list)
complain_pattern=re.compile(r'<table cellpadding="0" cellspacing="0" class="ar_c ar_c1">(.*?)</table>')
complain_pattern2=re.compile(r'<td>(.*?)</td><td .*?>(.*?)</td><td>(.*?)</td><td class="tsjs"><a href=".*?" target="_blank">(.*?)</a></td><td class="tsgztj">.*?,</td><td>(.*?)</td><td><img title="信息审核" src=".*?"><em>(.*?)</em></td>')

for j in url_list:
    response_complains = requests.get(headers=headers, url=j['url'])
    complains_temp = complain_pattern.findall(response_complains.text)
    print(response_complains.text)
    print(complains_temp)
    for complain in complains_temp:
        complains = complain_pattern2.findall(complain)
        with open('complains.csv','wb',encoding='utf-8') as file:
            file.writelines(complains)
