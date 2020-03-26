# 노트북 안에서 그래프를 그리기 위해
%matplotlib inline
# %matplotlib nbagg
    
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import qgrid
plt.rcParams['figure.figsize'] = [10, 6]

import warnings
warnings.filterwarnings('ignore')

import matplotlib as mpl
mpl.font_manager._rebuild()
mpl.pyplot.rc('font', family='NanumBarunGothic')

from IPython.display import Image
from IPython.display import display

from plotly import __version__
print (__version__)
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import plotly.figure_factory as ff

# Display all cell outputs
from IPython.core.interactiveshell import InteractiveShell

# Jupyter setup
# init_notebook_mode(connected=True)

import ipywidgets as widgets


df = pd.read_csv('C:/Users/User/Documents/GitHub/data-science-with-excel-master/민간아파트분양가격__p249.csv', encoding="cp949")

df['분양가격(㎡)'] = df['분양가격(㎡)'].dropna()
df['날짜'] = df['날짜'].dropna()

df['분양가격(㎡)'] = pd.to_numeric(df['분양가격(㎡)'], errors = 'coerce')
df['날짜'] = pd.to_datetime(df['날짜'], errors = 'coerce')

fig = px.line(df, x =df['날짜'], y = df['분양가격(㎡)'], title='df')
fig.show()



