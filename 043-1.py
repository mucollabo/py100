from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile

# DART 전자공시 사이트 APT 인증키 입력
crtfc_key = 'fa25647bb27b9b9911c8b5f0e2f6b7ae6a294df3'

# 회사의 고유번호 데이터를 불러오는 작업
corp_code = '00164742'
url = 'https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key='+crtfc_key
with urlopen(url) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        zfile.extractall('corp_num')