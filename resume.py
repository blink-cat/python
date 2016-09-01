from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl import load_workbook
import requests,json,matplotlib,pymysql
head={
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Content-Length':56,
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
#'Cookie':plusRecTip=0; td_cookie=803029566; LGMOID=20160829091430-03389892B79D9F0CE796D459E44C101A; user_trace_token=20160829091435-79e967ccf4594fb98d3c3ac730108e1c; LGUID=20160829091435-f2f7cf0e-6d85-11e6-8923-5254005c3644; HISTORY_POSITION=2270264%2C10k-19k%2C%E4%BA%AC%E4%B8%9C%2C%E5%95%86%E4%B8%9A%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%7C; td_cookie=797299066; JSESSIONID=CD25747FC043F0B09797ED730F7966E4; _putrc=68A2491DC7B1AB94; login=true; unick=%E6%9D%A8; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; SEARCH_ID=15d0cdef78814f5c87411cca2cd5d9f2; index_location_city=%E6%B7%B1%E5%9C%B3; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1472433228; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1472521303; LGSID=20160830092203-28518ba8-6e50-11e6-9efb-525400f775ce; LGRID=20160830094226-01731f5c-6e53-11e6-89bb-5254005c3644; _ga=GA1.2.1755439571.1472433229; ctk=1472521992
'Host':'www.lagou.com',
'Origin':'http://www.lagou.com',
'Referer':'http://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98?labelWords=&fromSearch=true&suginput=',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
'X-Anit-Forge-Code':0,
'X-Anit-Forge-Token':None,
'X-Requested-With':'XMLHttpReques',
}
url='http://www.lagou.com/jobs/positionAjax.json?px=default&city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false'
raw_json,company_name,position_id=[],[],[]
f_out=open('C:/Users/yangmengcheng/Desktop/json.json','w+')
conn=pymysql.connect('localhost','root','123SQL','company').cursor()
for pageid in range(1,30):
	data={'first':'true','pn':pageid,'kd':'数据挖掘'}
	if pageid>1:
		data['first']='false'
	else:	
		data['first']='false'
	response=requests.post(url,headers=head,data=data)
	company_json={i:response.json()['content']['positionResult'][i] for i in  response.json()['content']['positionResult'] if i=='result'}
	
	f_out.write(str(raw_json))
	company=response.json()['content']['positionResult']['result']
	for com_iter in company:
		#print(i['companyFullName'])
		company_name.append(com_iter['companyFullName'])


lista=set(company_name)
#print(lista)
#print(len(company_name))