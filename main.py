import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
	latest_iteration.text(f'Iteration {i+1}')
	bar.progress(i+1)
	time.sleep(0.1)




left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
	right_column.write('ここは右カラム')

expander1 = st.beta_expander('会社名')
expander1.write('株式会社まるまる')

expander2 = st.beta_expander('住所')
expander2.write('東京都丸の内')

expander3 = st.beta_expander('電話番号')
expander3.write('03-3333-3333')

text = st.text_input('あなたの趣味を教えてください。')


condition = st.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味は、', text, '　です。'

'コンディション：', condition

# if st.checkbox('Show Image'):
# 	img = Image.open('sample.jpg')
# 	st.image(img, caption='Mac sample image', use_column_width=True)



