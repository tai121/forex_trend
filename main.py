import streamlit as st
import os
import pandas as pd
import numpy as np
from scipy.signal import savgol_filter
import pandas_ta as ta
import logging
import platform
from datetime import datetime
import subprocess

# Chạy lệnh "ls" và lấy kết quả đầu ra
# result = subprocess.run(['ls'], capture_output=True, text=True)

# In kết quả đầu ra
print(result.stdout)

# df = df.drop(columns = ['Date'])
# st.write(df.shape[1])
st.write(platform.system())
st.write(datetime.now())
