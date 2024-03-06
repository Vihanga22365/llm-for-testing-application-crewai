import streamlit as st
from dotenv import load_dotenv
import os

os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="LLM for Testing - CrewAI - Frontend Testing", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>            
.stButton > button {
    width: 100%;
    height: 50px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Frontend Testing</h1>", unsafe_allow_html=True)
back_to_main = st.button('Back To Main Menu', key='back_to_main', type="secondary", help="Click for Main Menu")


st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

col1, col2 = st.columns(2)

with col1:
    if st.button('Frontend Test Cases Writing', key='test_cases_button', type="primary", use_container_width=True, help="Click for Write Frontend Test Cases"):
        st.switch_page("pages/6_Frontend_Test_Cases_Writing.py")

with col2:
    if st.button('Frontend Script Writing', key='script_write_button', type="primary", use_container_width=True, help="Click for Write Frontend Script Writing"):
        st.switch_page("pages/7_Frontend_Script_Writing.py")

if back_to_main:
    st.switch_page("1_Home_Page.py")


