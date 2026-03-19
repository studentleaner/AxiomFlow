import streamlit as st
import subprocess

def render():
    st.header("CLI Runner Interface")
    st.write("Commands triggered here are entirely executed as `subprocess.run(['axiomflow', ...])` to preserve standard terminal execution paths.")
    
    workflow_name = st.text_input("Workflow Name", placeholder="e.g. workflow.support_router")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Build Workflow via CLI"):
            if workflow_name:
                with st.spinner("Piping to axiomflow build..."):
                    result = subprocess.run(["axiomflow", "build", workflow_name], capture_output=True, text=True)
                    if result.returncode == 0:
                        st.success(result.stdout)
                    else:
                        st.error(result.stderr or result.stdout)
    with col2:
        if st.button("Run Workflow via CLI"):
            if workflow_name:
                with st.spinner("Piping to axiomflow run..."):
                    result = subprocess.run(["axiomflow", "run", workflow_name], capture_output=True, text=True)
                    if result.returncode == 0:
                        st.success(result.stdout)
                    else:
                        st.error(result.stderr or result.stdout)
