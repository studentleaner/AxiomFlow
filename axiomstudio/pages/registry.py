import streamlit as st
from axiomstudio import api
import copy

def render():
    st.header("Registry Browser")
    st.write("Browse templates, prompts, skills, and versions.")

    items = api.list_registry()
    if not items:
        st.info("No registry items found.")
        return

    col1, col2 = st.columns(2)
    with col1:
        search_term = st.text_input("Search ID").lower()
    with col2:
        types_available = ["All"] + list(set([i.get("type", "unknown") for i in items]))
        selected_type = st.selectbox("Filter by Type", types_available)

    filtered_items = []
    for real_item in items:
        # Deep copy to manipulate tags locally 
        item = copy.deepcopy(real_item)
        
        if search_term and search_term not in item['id'].lower():
            continue
        if selected_type != "All" and item.get('type') != selected_type:
            continue
        
        # Format tags
        tags = item.get("tags", [])
        if isinstance(tags, list):
            item["tags"] = ", ".join(tags)
            
        filtered_items.append(item)

    st.table(filtered_items)

    st.subheader("Item Details")
    options = [""] + [i["id"] for i in filtered_items]
    selected_id = st.selectbox("Select an item to view details:", options)
    if selected_id:
        data = api.get_registry_item(selected_id)
        st.json(data)
