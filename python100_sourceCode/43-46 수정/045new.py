import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

# DART 전자공시 사이트 APT 인증키 입력
my_auth_key = "---발급받은 개인 키를 입력하세요---"

# 종목코드를 고유변호로 변환
def get_code(stock_code):
    
    # 고유번호 리스트 파일 불러오기 
    XML_PATH = "./data/CORPCODE.xml"
    infile = open(XML_PATH,"r", encoding='utf-8')
    code_xml = infile.read()
    soup_xml = BeautifulSoup(code_xml,'html.parser')

    # 종목코드를 찾고, 고유번호를 추출
    items = soup_xml.find_all('list')   
    for item in items:
        scode = item.find('stock_code').text
        if str(scode)==str(stock_code):
            corp_code = item.find('corp_code').text
            print(corp_code)
            return corp_code
        
    print('Failed to get the proper code...')
    
    return None


# 검색기간 설정하기
now = dt.datetime.now()    
search_period = dt.timedelta(days=30)   
now_date = now.strftime('%Y%m%d')
start_date = (now-search_period).strftime('%Y%m%d')   
page_set = 10 

# DART 상세점보 접속 URL
crp_cd = get_code("005380")
url = "https://opendart.fss.or.kr/api/list.xml?crtfc_key="+my_auth_key+"&corp_code="+crp_cd\
      +"&page_count="+str(page_set)+"&bgn_de="+start_date


# BeautifulSoup으로 API가 반환하는 XML 해석하여 dataframe으로 정리
xml = requests.get(url)
soup = BeautifulSoup(xml.text, 'html.parser')  
print(str(soup)[:500])

search_result = pd.DataFrame()
items=soup.find_all('list')
print(len(items))

for item in items:
    temp_dataframe=pd.DataFrame(([[item.corp_cls.text, item.corp_name.text, item.stock_code.text,
                                   item.report_nm.text, item.rcept_no.text, item.flr_nm.text,
                                   item.rcept_dt.text, item.rm.text]]),
    columns=["corp_cls","corp_name","stock_code","report_nm","rcept_no","flr_nm","rcept_dt","rm"])
    search_result=pd.concat([search_result,temp_dataframe])

print(search_result)