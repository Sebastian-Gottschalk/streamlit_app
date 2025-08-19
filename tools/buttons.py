import streamlit as st

def tab1click():
    st.session_state.tab1 = True
    st.session_state.tab2 = False

def tab2click():
    st.session_state.tab2 = True
    st.session_state.tab1 = False