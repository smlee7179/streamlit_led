import streamlit as st
import requests
import pandas as pd
import time

# ThingSpeak 채널 정보
channel_id = 2232414  # 여기에 자신의 채널 ID를 넣으세요.
read_api_key = 'ZWFPB90A2ITQUVNP'  # 여기에 자신의 ThingSpeak Read API 키를 넣으세요.

# ThingSpeak API 엔드포인트 URL
url = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={read_api_key}&results=10'

# Streamlit 앱 제목
st.title('ThingSpeak 데이터 실시간 모니터링')

# 데이터를 업데이트하는 함수
def update_data():
    try:
        response = requests.get(url)
        data = response.json()
        feeds = data['feeds']
        df = pd.DataFrame(feeds)
        df['created_at'] = pd.to_datetime(df['created_at'])
        return df
    except:
        return None

# 실시간 데이터 시각화
while True:
    df = update_data()
    if df is not None:
        st.write(df)
    else:
        st.write('데이터를 가져올 수 없습니다.')
    time.sleep(10)  # 10초마다 데이터 업데이트
