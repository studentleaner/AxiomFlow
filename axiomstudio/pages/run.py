import streamlit as st
import json
from axiomstudio import api

def render():
    st.header("Execute Workflow")
    st.write("Trigger configuration endpoints executing dynamically tracking traces strictly natively gracefully elegantly successfully securely")

    workflows = api.list_workflows()
    if not workflows:
        st.warning("No dynamic mappings processed.")
        return

    options = [w["id"] for w in workflows]
    selected_workflow = st.selectbox("Select Target Workflow", options)

    st.subheader("Execution Parameters")
    inputs_str = st.text_area("Pass parameters structurally natively cleanly safely gracefully exclusively safely successfully", value='{"test": 1}')
    
    col1, _ = st.columns([1, 4])
    with col1:
        run_btn = st.button("Run Execution Instance", type="primary", use_container_width=True)

    if run_btn:
        try:
            inputs = json.loads(inputs_str)
        except Exception:
            inputs = {}
            st.error("JSON properties malformed.")
            
        with st.spinner(f"Spawning native execution bindings safely evaluating subprocess effectively `{selected_workflow}`..."):
            result = api.run_workflow(selected_workflow, inputs)
            
            if result.get("status"):
                st.success("Execution properly concluded.")
            else:
                st.error("Process execution crashed.")
                
            st.subheader("Process Results")
            if result.get("stdout"):
                st.text(result.get("stdout"))
            if result.get("stderr"):
                st.error(result.get("stderr"))
                
    st.markdown("---")
    st.subheader("Execution Trace Elements")
    logs = api.get_logs()
    for log in logs:
        st.text(f"[{log['timestamp']}] {log['level']}: {log['message']}")

    st.markdown("---")
    st.subheader("Execution Node Properties")
    st.write("Configured JSON values extracted explicitly cleanly properly decoupled structurally definitively securely purely natively explicitly.")
    plan = api.get_last_plan()
    if isinstance(plan, dict) and "message" in plan:
        st.info(plan["message"])
    elif isinstance(plan, dict) and "error" in plan:
        st.error(plan["error"])
    else:
        st.json(plan)
