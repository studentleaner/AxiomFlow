import streamlit as st
import os

def render():
    st.header("Standard YAML Configuration Editor")
    
    file_path = st.text_input("Raw file path target", placeholder="e.g. workflows/router.yaml")
    
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            content = f.read()
            
        new_content = st.text_area("Live Editor", value=content, height=450)
        
        if st.button("Save Changes to Disk"):
            # Saves purely to disk, doesn't validate execution graph
            with open(file_path, "w") as f:
                f.write(new_content)
            st.success("File strictly overwritten locally.")
    else:
        st.info("Input valid valid relative path to begin editing.")
