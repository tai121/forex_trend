import streamlit as st
import os
import pandas as pd
import numpy as np
from scipy.signal import savgol_filter
import pandas_ta as ta
import logging
import platform
from datetime import datetime
url = 'https://anaconda.org/conda-forge/libta-lib/0.4.0/download/linux-64/libta-lib-0.4.0-h166bdaf_1.tar.bz2'
os.system('curl -L $url | tar xj -C /usr/lib/x86_64-linux-gnu/ lib --strip-components=1')
url = 'https://anaconda.org/conda-forge/ta-lib/0.4.19/download/linux-64/ta-lib-0.4.19-py39hd257fcd_4.tar.bz2'
os.system('curl -L $url | tar xj -C /usr/local/lib/python3.9/dist-packages/ lib/python3.9/site-packages/talib --strip-components=3')
df = pd.read_csv('data_after_processing.csv')
days = 30
df['Target'] = np.where((df['Close'].shift(30) > df['Close']), 1, 0)
window_size = 33
poly_order = 2

df['Close'] = savgol_filter(df['Close'], window_size, poly_order)
df.ta.log_return(cumulative=True, append=True)
df.ta.percent_return(cumulative=True, append=True)
try:
    df.ta.strategy(ta.AllStrategy)
except :
    logging.info("lỗi pandas_ta")

df = df.drop(columns = ['Date'])
st.write(platform.system())
st.write(datetime.now())
