import streamlit as st
from axiomstudio import api

def render():
    st.header("Workflows List")
    st.write("View available execution graphs and configurations.")

    workflows = api.list_workflows()
    if not workflows:
        st.info("No workflows found in directory.")
        return

    st.table(workflows)

    st.subheader("Workflow Details")
    options = [""] + [w["id"] for w in workflows]
    selected_id = st.selectbox("Select a workflow to inspect:", options)
    if selected_id:
        data = api.get_workflow(selected_id)
        
        st.write(f"**Description:** {data.get('description', 'No description provided')}")
        
        nodes = data.get("nodes", {})
        edges = data.get("edges", [])
        
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Nodes:** {len(nodes)}")
            st.json(nodes)
        with col2:
            st.write(f"**Edges:** {len(edges)}")
            st.json(edges)
