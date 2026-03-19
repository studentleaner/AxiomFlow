import streamlit as st
from axiomstudio import api
from axiomstudio.components import graph

def render():
    st.header("⚙️ Deployed Workflows")
    st.write("View compiled architecture topologies.")

    workflows = api.list_workflows()
    if not workflows:
        st.warning("No workflows discovered.")
        return

    st.markdown("---")
    selected_id = st.selectbox("Select Workflow", [w["id"] for w in workflows])

    if selected_id:
        data = api.load_workflow_file(selected_id)
        if not data:
            st.error("Missing physical workflow definition locally.")
            return

        st.subheader(f"Workflow: {data.get('name', selected_id)}")
        st.write(f"**Description**: {data.get('description', 'N/A')}")
        
        tab1, tab2 = st.tabs(["Graph View", "JSON Definition"])
        
        with tab1:
            nodes = data.get("nodes", [])
            edges = data.get("edges", [])
            if not nodes:
                st.info("Workflow has no processing nodes configured natively yet.")
            else:
                graph.render_simple_graph(nodes, edges)

        with tab2:
            st.json(data)
