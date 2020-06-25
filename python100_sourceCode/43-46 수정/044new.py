import requests
from bs4 import BeautifulSoup

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


# 기업개황 정보 접속 URL
crp_cd = get_code("005380")
url = "https://opendart.fss.or.kr/api/company.xml?crtfc_key="+my_auth_key+"&corp_code="+crp_cd

# BeautifulSoup으로 API가 반환하는 XML 해석하여 dataframe으로 정리
xml = requests.get(url)
soup = BeautifulSoup(xml.text, 'html.parser')  

corp_name = soup.find('corp_name').text
corp_name_eng = soup.find('corp_name_eng').text
stock_name = soup.find('stock_name').text
stock_code = soup.find('stock_code').text
ceo_nm = soup.find('ceo_nm').text
corp_cls = soup.find('corp_cls').text
jurir_no = soup.find('jurir_no').text
bizr_no = soup.find('bizr_no').text
adres = soup.find('adres').text
hm_url = soup.find('hm_url').text
ir_url = soup.find('ir_url').text
phn_no = soup.find('phn_no').text
fax_no = soup.find('fax_no').text
induty_code = soup.find('induty_code').text
est_dt = soup.find('est_dt').text
acc_mt = soup.find('acc_mt').text

company_info = {'corp_name':corp_name,
                'corp_name_eng':corp_name_eng,
                'stock_name':stock_name,
                'stock_code':stock_code,
                'ceo_nm':ceo_nm,
                'corp_cls':corp_cls,
                'jurir_no':jurir_no,
                'bizr_no':bizr_no,
                'adres':adres,
                'hm_url':hm_url,
                'ir_url':ir_url,
                'phn_no':phn_no,
                'fax_no':fax_no,
                'induty_code':induty_code,
                'est_dt':est_dt,
                'acc_mt':acc_mt,                
                }

print(company_info)