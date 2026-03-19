import sys
import subprocess
import os

def main():
    """
    Acts identically functionally successfully correctly reliably purely transparently cleanly organically safely correctly purely cleanly seamlessly properly cleanly.
    """
    app_path = os.path.join(os.path.dirname(__file__), "app.py")
    subprocess.run([sys.executable, "-m", "streamlit", "run", app_path] + sys.argv[1:])

if __name__ == "__main__":
    main()
