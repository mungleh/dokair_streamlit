import streamlit as st
import pandas as pd
import requests
import json


st.set_page_config(page_title = "api dokair",
                   layout = "wide",
                   )


headers = {
   'accept': 'application/json',
   'Content-Type': 'application/json',
}

col1,col2 = st.columns(2)

with col1:
    sl = st.text_input('sepal_length', '0')
    sw = st.text_input('sepal_width', '0')
    pl = st.text_input('petal_length', '0')
    pw = st.text_input('petal_width', '0')

    if st.button('predict'):
        data = f'{{"sepal_length": {sl},"sepal_width": {sw},"petal_length": {pl},"petal_width": {pw}}}'
        response = requests.post('https://maxinaiskebabou.azurewebsites.net/predict', headers=headers, data=data)
        st.write(response.text)

        response_json = json.loads(response.text)
        prediction = response_json["prediction"]
        probability = response_json["probability"]

        truc = f"{sl} {sw} {pl} {pw}"

        inputs = {
            "input": truc,
            "prediction": prediction,
            "probabilité": probability
        }

        add = requests.post('https://maxinaiskebabou.azurewebsites.net/add', headers=headers, json=inputs)

    if st.button('clear'):
        delete = requests.post('https://maxinaiskebabou.azurewebsites.net/del', headers= headers)
        st.write(delete.text)


with col2:
    st.write('Inputs history')
    df = pd.DataFrame(requests.get('https://maxinaiskebabou.azurewebsites.net', headers=headers).json())
    st.dataframe(df)
