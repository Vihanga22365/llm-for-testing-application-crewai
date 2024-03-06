import streamlit as st
from dotenv import load_dotenv
import os

os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="LLM for Testing - CrewAI - Home" ,layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>            
.stButton > button {
    width: 100%;
    height: 50px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>LLM for Testing with Crew AI</h1>", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

col1, col2 = st.columns(2)

with col1:
    if st.button('Backend Testing', key='backend_button', type="primary", use_container_width=True, help="Click for Backend Testing"):
        st.switch_page("pages/2_Backend_Testing.py")

with col2:
    if st.button('Frontend Testing', key='frontend_button', type="primary", use_container_width=True, help="Click for Frontend Testing"):
        st.switch_page("pages/3_Frontend_Testing.py")


import streamlit as st
import subprocess

def get_specific_libraries_versions(libraries):
    # Use subprocess to execute `pip freeze` and capture the output
    result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)
    # Decode the output from bytes to string
    installed_libraries = result.stdout.decode('utf-8').split('\n')

    # Filter for the specific libraries
    specific_libraries_info = "\n".join([lib for lib in installed_libraries if any(spec_lib in lib for spec_lib in libraries)])
    return specific_libraries_info

def main():
    st.title('Check Specific Libraries Versions')

    libraries = ['streamlit']
    
    if st.button('Show Versions of Specific Libraries'):
        libraries_versions = get_specific_libraries_versions(libraries)
        if libraries_versions:
            # Display the versions of specific libraries
            st.text_area("Versions of specified libraries:", value=libraries_versions, height=200)
        else:
            st.write("None of the specified libraries are installed.")

if __name__ == "__main__":
    main()
