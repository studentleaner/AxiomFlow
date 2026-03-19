import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from axiomstudio.pages import dashboard, registry, workflows, run, editor

def main():
    st.set_page_config(page_title="AxiomStudio", layout="wide")
    st.sidebar.title("AxiomStudio Navigation")

    pages = ["Dashboard", "Workflows", "Registry", "Run", "Settings"]
    selection = st.sidebar.radio("Navigate", pages)

    if selection == "Dashboard":
        dashboard.render()
    elif selection == "Registry":
        registry.render()
    elif selection == "Workflows":
        workflows.render()
    elif selection == "Run":
        run.render()
    elif selection == "Editor":
        editor.render()
    else:
        st.warning(f"Feature '{selection}' is currently disabled in this initial implementation phase.")
        st.info("AxiomStudio integrates core logical structures flawlessly navigating seamlessly into isolated boundaries.")

if __name__ == "__main__":
    main()
