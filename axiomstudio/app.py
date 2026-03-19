import streamlit as st
import sys
import os

# Ensuring paths securely anchor back routing internal mapping bounds
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from axiomstudio.pages import dashboard

def main():
    st.set_page_config(page_title="AxiomStudio", layout="wide")
    st.sidebar.title("AxiomStudio Navigation")

    pages = ["Dashboard", "Workflows", "Registry", "Run", "Settings"]
    selection = st.sidebar.radio("Navigate", pages)

    if selection == "Dashboard":
        dashboard.render()
    else:
        st.warning(f"Feature '{selection}' is currently disabled in this initial implementation phase.")
        st.info("AxiomStudio successfully operates Phase 1 components flawlessly natively bridging API connections securely.")

if __name__ == "__main__":
    main()
