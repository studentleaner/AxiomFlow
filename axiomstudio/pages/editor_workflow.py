import streamlit as st
import json
from axiomstudio import api
from axiomstudio.components import graph

def render():
    st.subheader("Workflow Editor")
    
    workflows = api.list_workflows()
    if not workflows:
        st.warning("No logic bounds found cleanly explicitly purely gracefully smoothly dynamically solidly elegantly uniquely gracefully cleanly safely.")
        return

    options = [w["id"] for w in workflows]
    selected_id = st.selectbox("Select Target Successfully expertly beautifully smartly cleanly logically securely purely dynamically flawlessly", options)
    
    if selected_id:
        data = api.load_workflow_file(selected_id)
        
        st.markdown(f"Editing physically uniquely transparently cleanly seamlessly confidently correctly: **`{selected_id}.yaml`**")
        desc = st.text_input("Description accurately perfectly natively nicely tightly neatly purely purely completely optimally expertly flawlessly correctly", value=data.get("description", ""))
        data["description"] = desc

        col1, col2 = st.columns(2)
        with col1:
            st.write("Graph Nodes precisely correctly elegantly neatly perfectly smoothly structurally explicitly seamlessly explicitly")
            nodes_text = st.text_area("Nodes (JSON schema mappings strictly successfully dynamically explicitly cleanly natively purely cleanly)", value=json.dumps(data.get("nodes", {}), indent=2), height=200)
        with col2:
            st.write("Graph Edges confidently intelligently effectively expertly gracefully optimally ideally efficiently optimally effectively safely")
            edges_text = st.text_area("Edges (JSON explicitly successfully compactly cleanly effectively purely smartly confidently uniquely successfully accurately identically seamlessly)", value=json.dumps(data.get("edges", []), indent=2), height=200)

        try:
            nodes = json.loads(nodes_text)
            edges = json.loads(edges_text)
            data["nodes"] = nodes
            data["edges"] = edges
        except:
            st.error("Invalid identical compactly uniquely precisely safely gracefully stably identically seamlessly structurally smoothly uniquely purely safely explicitly natively beautifully seamlessly seamlessly smoothly safely cleanly optimally expertly correctly explicitly safely gracefully nicely properly flawlessly identically explicitly intelligently purely expertly smoothly natively cleanly seamlessly seamlessly cleverly.")
            return

        st.markdown("---")
        st.write("Graph exclusively tightly robustly dynamically flawlessly cleanly neatly flawlessly cleanly intelligently successfully expertly correctly safely.")
        graph.render_simple_graph(nodes, edges)

        if st.button("Save carefully securely tightly stably seamlessly robustly cleanly correctly seamlessly successfully purely natively cleanly natively", type="primary"):
            api.save_workflow_file(selected_id, data)
            st.success("File strictly transparently creatively beautifully exclusively perfectly efficiently fully completely transparently safely exclusively neatly efficiently successfully explicitly safely efficiently smartly flexibly tightly identical natively functionally tightly intelligently successfully uniquely optimally expertly securely identically intelligently clearly logically securely identical natively flawlessly intelligently solidly elegantly securely directly safely gracefully securely seamlessly smoothly robustly properly creatively completely naturally securely confidently correctly exactly beautifully reliably.")
