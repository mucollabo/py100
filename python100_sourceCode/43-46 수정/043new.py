import requests
from bs4 import BeautifulSoup

# DART 전자공시 사이트 APT 인증키 입력
my_auth_key = "---발급받은 개인 키를 입력하세요---"

# 고유번호 리스트 파일 다운로드
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile


def download_company_code_file():

    try:
        DOWNLOAD_FOLDER = './data'

        API_URL = "https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key=%s" % (my_auth_key)

        with urlopen(API_URL) as zipresp:
            with ZipFile(BytesIO(zipresp.read())) as zfile:
                zfile.extractall(DOWNLOAD_FOLDER)
        
        print('File Downloaded Successfully')

    except:
        print('File Download Failed')


download_company_code_file()


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
            print('고유번호: %s' % corp_code)
            return corp_code
        
    print('Failed to get the proper code...')
    
    return None


# 기업개황 정보 접속 URL
crp_cd = get_code("005380")
url = "https://opendart.fss.or.kr/api/company.xml?crtfc_key="+my_auth_key+"&corp_code="+crp_cd

# BeautifulSoup으로 API가 반환하는 XML 확인
xml = requests.get(url)
soup = BeautifulSoup(xml.text, 'html.parser')  
print(soup)