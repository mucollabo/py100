from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re

def read_danawa_wishlist():

    driver = webdriver.Chrome("../Selenium/chromedriver")
    driver.implicitly_wait(3)
    driver.get("https://www.danawa.com/")

    # 다나와 메인화면의 로그인 버튼을 누르는 작업 실행
    login = driver.find_element_by_css_selector('li.my_page_service > a')
    login.click()
    driver.implicitly_wait(3)

    # 아이디/비밀번호를 입력하고 로그인하기 버튼을 누르는 작업 실행
    my_id = "vw0901"
    my_pw = "qjcndjfw1!"

    driver.find_element_by_id('danawa-member-login-input-id').send_keys(my_id)
    driver.implicitly_wait(2)
    driver.find_element_by_name('password').send_keys(my_pw)
    driver.implicitly_wait(2)
    driver.find_element_by_css_selector('button.btn_login').click()
    driver.implicitly_wait(2)

    # 관심상품 목록 HTML 페이지 가져오기
    driver.find_element_by_css_selector('li.interest_goods_service > a').click()
    driver.implicitly_wait(2)
    html_src = driver.page_source
    driver.close()

    # 관심상품 목록 HTML 페이지를 BeautifulSoup으로 파싱하고, 데이터프레임으로 정리하기
    soup = BeautifulSoup(html_src, 'lxml')

    wish_table = soup.select('table[class="tbl wish_tbl"]')[0]
    wish_items = wish_table.select('tbody tr')

    titles = []
    prices = []
    links = []

    for item in wish_items:
        title = item.find('div', {'class': 'tit'}).text
        price = item.find('span', {'class': 'price'}).text
        link = item.find('a', href=re.compile('prod.danawa.com/info/')).get('href')

        titles.append(title)
        prices.append(price)
        links.append(link)

        result = {'title': titles, 'price': prices, 'link': links}

    data = pd.DataFrame(result)

    return data

data = read_danawa_wishlist()
print(data, '\n')

for idx in data.index:
    data.loc[idx, 'id'] = idx + 1

print(data, '\n')

print(data.price)
data.price = data.price.str.replace('원', '')
data.price = data.price.str.replace(',', '')
data.price = data.price.astype('int')
print(data.price)
data.id = data.id.astype('int')
print(data.id)
print('\n')

update_db = data.set_index('id')
print(update_db, '\n')

# 데이터프레임을 DB에 업로드 (테이블 추가)
import sqlite3
import os
db_file = os.path.join(os.getcwd(), 'danawa.sqlite')
conn = sqlite3.connect(db_file)
update_db.to_sql('Product', conn, if_exists='replace')

# DB 테이블 내용 확인
cur = conn.cursor()
cur.execute('SELECT * from Product')
rows = cur.fetchall()
for row in rows:
    print(row)

# DB 연결 종료
conn.close()
