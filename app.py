import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
# import plotly.express as px
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pickle
import requests


st.set_page_config(page_title = "api dokair",
                   layout = "wide",
                   )


url = 'https://maxinaiskebabou.azurewebsites.net//predict'


headers = {
   'accept': 'application/json',
   'Content-Type': 'application/json',
}

sl = st.text_input('sepal_length', '0')
sw = st.text_input('sepal_width', '0')
pl = st.text_input('petal_length', '0')
pw = st.text_input('petal_width', '0')

if st.button('predict'):
    data = f'{{"sepal_length": {sl},"sepal_width": {sw},"petal_length": {pl},"petal_width": {pw}}}'
    response = requests.post(url, headers=headers, data=data)
    st.write(response.text)
