import streamlit as st
import json
from axiomstudio import api
from axiomstudio.components import graph

def render():
    st.header("📝 Workflow Editor")
    
    workflows = api.list_workflows()
    if not workflows:
        st.warning("No workflows found.")
        return

    options = [w["id"] for w in workflows]
    selected_id = st.selectbox("Select Workflow", options)
    
    if selected_id:
        data = api.load_workflow_file(selected_id)
        
        st.markdown(f"Editing: **`{selected_id}.yaml`**")
        desc = st.text_input("Description", value=data.get("description", ""))
        data["description"] = desc

        col1, col2 = st.columns(2)
        with col1:
            st.write("Graph Nodes")
            nodes_text = st.text_area("Nodes (JSON)", value=json.dumps(data.get("nodes", {}), indent=2), height=200)
        with col2:
            st.write("Graph Edges")
            edges_text = st.text_area("Edges (JSON)", value=json.dumps(data.get("edges", []), indent=2), height=200)

        try:
            nodes = json.loads(nodes_text)
            edges = json.loads(edges_text)
            data["nodes"] = nodes
            data["edges"] = edges
        except:
            st.error("Invalid JSON representation.")
            return

        st.markdown("---")
        with st.expander("Topology Graph Visualization", expanded=True):
            graph.render_simple_graph(nodes, edges)

        st.markdown("---")
        if st.button("Save Workflow", type="primary"):
            api.save_workflow_file(selected_id, data)
            st.success("File written successfully.")
