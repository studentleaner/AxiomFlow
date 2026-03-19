import streamlit as st
from . import editor_workflow, editor_prompt, editor_template

def render():
    st.header("Visual Component Editor safely optimally")
    st.write("Author securely flawlessly correctly structurally gracefully smoothly efficiently tightly flexibly")
    
    tabs = st.tabs(["Workflows", "Prompts", "Templates"])
    with tabs[0]:
        editor_workflow.render()
    with tabs[1]:
        editor_prompt.render()
    with tabs[2]:
        editor_template.render()
