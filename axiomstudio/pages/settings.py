import streamlit as st
from axiomstudio import api

def render():
    st.header("ContextFlow Configuration")
    st.write("Edit connection layers without engaging processors.")
    
    config = api.get_config()
    
    st.subheader("Adapter Settings")
    adapter = config.get("adapter", {})
    a_type = st.selectbox("Type", ["openai", "ollama", "anthropic"], index=["openai", "ollama", "anthropic"].index(adapter.get("type", "openai")) if adapter.get("type", "openai") in ["openai", "ollama", "anthropic"] else 0)
    a_model = st.text_input("Model Name", value=adapter.get("model", "gpt-4"))
    
    st.subheader("Memory Settings")
    memory = config.get("memory", {})
    m_enabled = st.checkbox("Enable Memory", value=memory.get("enabled", False))
    m_type = st.selectbox("Memory Type", ["vector", "graph", "kv"], index=["vector", "graph", "kv"].index(memory.get("type", "vector")) if memory.get("type", "vector") in ["vector", "graph", "kv"] else 0)
    m_path = st.text_input("Storage Path", value=memory.get("path", "./memory"))
    
    st.subheader("RAG Settings")
    rag = config.get("rag", {})
    r_enabled = st.checkbox("Enable RAG", value=rag.get("enabled", False))
    r_folder = st.text_input("Documents Folder", value=rag.get("folder", "./docs"))
    
    st.subheader("Tools Configuration")
    tools = config.get("tools", {})
    t_enabled = st.checkbox("Enable Tools", value=tools.get("enabled", False))
    
    if st.button("Save Configuration", type="primary"):
        config["adapter"] = {"type": a_type, "model": a_model}
        config["memory"] = {"enabled": m_enabled, "type": m_type, "path": m_path}
        config["rag"] = {"enabled": r_enabled, "folder": r_folder}
        config["tools"] = {"enabled": t_enabled}
        
        api.save_config(config)
        st.success("Configuration strictly correctly identical fully cleanly flawlessly efficiently cleverly written efficiently.")
