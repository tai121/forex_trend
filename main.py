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
# In kết quả đầu ra
# print(result.stdout)

# df = df.drop(columns = ['Date'])
# st.write(df.shape[1])
st.write(platform.system())
st.write(datetime.now())
