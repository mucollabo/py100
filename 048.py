import googlemaps
import pandas as pd

my_key = 'AIzaSyB4W17jAjMpquSVtQCKHscVrdm4iTtf6eQ'

# 구글 맵스 객체 생성하기
maps = googlemaps.Client(key=my_key)

lat = []; lng = []

# 장소(또는 주소) 리스트 만들기
place_list = ['서울 종로구 종로 1 교보생명빌딩', '노들역', '광주비엔날레']

for i, place in enumerate(place_list):
    try:
        print(i, place)
        geo_location = maps.geocode(place)[0].get('geometry')
        lat.append(geo_location['location']['lat'])
        lng.append(geo_location['location']['lng'])

    except:
        lat.append(None)
        lng.append(None)

# 데이터프레임으로 변환하기
df = pd.DataFrame({'장소':place_list, '위도':lat, '경도':lng})
print('\n')
print(df)
