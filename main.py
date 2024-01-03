#import library yang di butuhkan

import streamlit as st
from web_function import load_data

from Tabs import home, predict, visualise

Tabs = {
    "home" : home,
    "prediction" : predict,
    "visualisasion" : visualise,
}

# membuat sidber
st.sidebar.title("navigasi")

#membuat  radio opsion
page = st.sidebar.radio("pages",list(Tabs.keys()))

#load dataset
df, x, y = load_data

#komunikasi call app fuction
if page in ["prediction","visualisation"]:
    Tabs[page].app(df, x, y)
else:
    Tabs[page].app()