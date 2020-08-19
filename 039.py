from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import os

# 검색 keyword, 검색 기간 입력
keyword1 = 'apple iphone'
keyword2 = 'samsung galaxy'
keyword3 = 'music'
keyword4 = 'collaboration'
keyword5 = 'COVID-19'
period = 'today 5-y'

# Google Trend 접속 및 데이터 탑재
trend_obj = TrendReq()
trend_obj.build_payload(kw_list=[keyword1, keyword2, keyword3, keyword4, keyword5], timeframe=period)
trend_df = trend_obj.interest_over_time()

# 그래프 출력
plt.style.use('ggplot')
plt.figure(figsize=(14, 5))
trend_df[keyword1].plot()
trend_df[keyword2].plot()
trend_df[keyword3].plot()
trend_df[keyword4].plot()
trend_df[keyword5].plot()
plt.title('Google Trends: %s, %s, %s, %s, %s' % (keyword1, keyword2, keyword3, keyword4, keyword5), size=15)
plt.legend(loc='best')

# 그래프 파일 저장
cwd = os.getcwd()
output_filepath = os.path.join(cwd, 'output', 'google_trend_%s_vs_%s.png' %(keyword1, keyword2))
plt.savefig(output_filepath, dpi=300)
plt.show()
