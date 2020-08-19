import requests
from bs4 import BeautifulSoup

# DART 전자공시 사이트 APT 인증키 입력
crtfc_key = 'fa25647bb27b9b9911c8b5f0e2f6b7ae6a294df3'

# 기업개황 정보 접속 URL
corp_code = '00164742'
url = 'https://opendart.fss.or.kr/api/company.xml?crtfc_key='+crtfc_key+'&corp_code='+corp_code

# BeautifulSoup으로 API가 반환하는 XML 확인
xml = requests.get(url)
soup = BeautifulSoup(xml.text, 'html.parser')
print(soup)