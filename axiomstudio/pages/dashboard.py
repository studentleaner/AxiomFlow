import streamlit as st
from axiomstudio import api

def render():
    st.header("🏠 AxiomStudio Dashboard")
    st.write("Overview of your AI Workspace configurations.")

    workflows = api.list_workflows()
    registry_items = api.list_registry()

    adapters_count = 3  
    last_runs_count = 12  

    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("⚙️ Workflows", len(workflows))
    with col2:
        st.metric("📚 Registry Items", len(registry_items))
    with col3:
        st.metric("🔌 Adapters", adapters_count)
    with col4:
        st.metric("⏱️ Last Runs", last_runs_count)

    st.markdown("---")
    st.subheader("System Activity")
    st.info("System foundational logic mapped correctly. Awaiting deployment of feature logic components.")
