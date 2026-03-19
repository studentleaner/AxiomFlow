import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from axiomstudio.pages import dashboard, registry, workflows, run, editor, settings

def main():
    st.set_page_config(page_title="AxiomStudio", layout="wide")
    st.sidebar.title("Navigation")

    pages = {
        "🏠 Dashboard": dashboard.render,
        "📚 Registry": registry.render,
        "⚙️ Workflows": workflows.render,
        "▶️ Run": run.render,
        "📝 Editor": editor.render,
        "🛠️ Settings": settings.render
    }
    
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    pages[selection]()

if __name__ == "__main__":
    main()
