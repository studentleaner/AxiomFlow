import streamlit as st
import subprocess
from axiomflow.ui import viewer, editor, runner

def main():
    st.set_page_config(page_title="AxiomFlow UI", layout="wide")
    st.title("AxiomFlow UI - Local Thin Client")
    
    st.sidebar.header("Navigation")
    choice = st.sidebar.radio("Go to", ["Home", "Viewer", "Editor", "Runner"])
    
    if choice == "Home":
        st.write("Welcome to the final iteration layer for AxiomFlow.")
        st.info("This application is entirely detached from the underlying Axiom core and ContextFlow engines. Every action leverages the CLI wrapper (`axiomflow run`, `axiomflow build`) exclusively.")
        if st.button("Test CLI Connection"):
            try:
                # Subprocess isolated strictly
                result = subprocess.run(["axiomflow", "--help"], capture_output=True, text=True)
                if result.returncode == 0:
                    st.success("Verified: Internal CLI successfully reached.")
            except Exception as e:
                st.error(f"Cannot locate installed CLI route: {e}")
                
    elif choice == "Viewer":
        viewer.render()
    elif choice == "Editor":
        editor.render()
    elif choice == "Runner":
        runner.render()

if __name__ == "__main__":
    # If run generically through scripting
    main()
