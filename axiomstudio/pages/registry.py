import streamlit as st
import pandas as pd
from axiomstudio import api

def render():
    st.header("📚 Registry Browser")
    st.write("Browse templates, prompts, and skills currently available natively.")

    items = api.list_registry()
    if not items:
        st.warning("No registry items found.")
        return

    df = pd.DataFrame(items)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        type_filter = st.selectbox("Filter by Type", ["All"] + list(df["type"].unique()))
    with col2:
        search_query = st.text_input("Search (ID or Name)")

    if type_filter != "All":
        df = df[df["type"] == type_filter]
    
    if search_query:
        df = df[df["id"].str.contains(search_query, case=False, na=False) | df["name"].str.contains(search_query, case=False, na=False)]

    st.markdown("---")
    st.dataframe(df[["id", "type", "name", "description"]], use_container_width=True)

    st.markdown("---")
    st.subheader("Item Inspection")
    selected_id = st.selectbox("Select Item to Inspect", df["id"].tolist())
    
    if selected_id:
        item_data = api.load_registry_item(selected_id)
        if item_data:
            st.json(item_data)
        else:
            st.error("Failed to load item.")
