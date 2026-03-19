import streamlit as st
import json
from axiomstudio import api

def render():
    st.subheader("Prompt Editor")
    
    items = api.list_registry()
    prompts = [i["id"] for i in items if i["type"] in ["prompt", "template"]]
    
    if not prompts:
        st.warning("No prompts found.")
        return

    selected_id = st.selectbox("Select Prompt", prompts)
    
    if selected_id:
        data = api.load_registry_item(selected_id)
        
        st.markdown(f"Editing: **`{selected_id}.yaml`**")
        name = st.text_input("Name", value=data.get("name", ""))
        desc = st.text_input("Description", value=data.get("description", ""))
        content = st.text_area("Template Text", value=data.get("template", ""), height=300)
        
        data["name"] = name
        data["description"] = desc
        data["template"] = content
        
        if st.button("Save Prompt", type="primary"):
            api.save_registry_file(selected_id, data)
            st.success("File written successfully.")
