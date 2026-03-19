import streamlit as st
import os
import json

def render():
    st.header("Local Definitions Viewer")
    st.write("Visualizes structured contents on standard filesystem bounds.")
    
    path = st.text_input("Target Directory to Scan", value="registry/")
    if os.path.exists(path) and os.path.isdir(path):
        files = os.listdir(path)
        selected_file = st.selectbox("Select object", files)
        if selected_file:
            target = os.path.join(path, selected_file)
            with open(target, "r") as f:
                content = f.read()
            if target.endswith(".json"):
                try:
                    st.json(json.loads(content))
                except:
                    st.code(content, language="json")
            else:
                st.code(content, language="yaml")
    else:
        st.warning("Path unresolvable or does not exist locally.")
